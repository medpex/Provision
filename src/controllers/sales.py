from flask import request, jsonify
from flask import Blueprint
from src.app import db
from src.models.sale import Sale
from src.controllers.auth import commission_manager_required
from src.engine.notifications import send_new_sale_notification

bp = Blueprint('sales', __name__)

@bp.route('/sales', methods=['POST'])
@commission_manager_required
def create_sale(current_user):
    data = request.get_json()
    new_sale = Sale(
        user_id=data['user_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        sale_date=data['sale_date']
    )
    db.session.add(new_sale)
    db.session.commit()
    send_new_sale_notification(new_sale)
    return jsonify({'message': 'New sale created.'}), 201

from src.controllers.auth import token_required

@bp.route('/sales', methods=['GET'])
@token_required
def get_sales(current_user):
    sales = Sale.query.filter_by(user_id=current_user.id).all()
    output = []
    for sale in sales:
        sale_data = {}
        sale_data['id'] = sale.id
        sale_data['user_id'] = sale.user_id
        sale_data['product_id'] = sale.product_id
        sale_data['quantity'] = sale.quantity
        sale_data['sale_date'] = sale.sale_date
        output.append(sale_data)
    return jsonify({'sales': output})
