from flask import request, jsonify, Blueprint
from src.engine.commission_engine import CommissionEngine
from src.engine.commission_rules import FlatRateRule, TieredRateRule
from src.models.product import Product
from src.models.sale import Sale

bp = Blueprint('simulation', __name__)

@bp.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    hypothetical_sales = []
    for sale_data in data['sales']:
        product = Product.query.get(sale_data['product_id'])
        hypothetical_sales.append(
            Sale(
                product=product,
                quantity=sale_data['quantity']
            )
        )

    # In a real application, the rules would be loaded from the database
    # or a configuration file.
    rules = [
        TieredRateRule({1000: 0.1, 2000: 0.15, 5000: 0.2}),
        FlatRateRule(0.05)
    ]
    engine = CommissionEngine(rules)

    total_commission = 0
    for sale in hypothetical_sales:
        total_commission += engine.calculate(sale)

    return jsonify({'projected_commission': total_commission})
