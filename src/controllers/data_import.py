import os
from flask import request, jsonify, Blueprint
from src.app import db
from src.models.sale import Sale
from src.controllers.auth import commission_manager_required
import pandas as pd

bp = Blueprint('data_import', __name__)

@bp.route('/upload/csv', methods=['POST'])
@commission_manager_required
def upload_csv(current_user):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            new_sale = Sale(
                user_id=row['user_id'],
                product_id=row['product_id'],
                quantity=row['quantity'],
                sale_date=row['sale_date']
            )
            db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'File uploaded and data imported successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid file type.'}), 400

@bp.route('/upload/excel', methods=['POST'])
@commission_manager_required
def upload_excel(current_user):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and (file.filename.endswith('.xls') or file.filename.endswith('.xlsx')):
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            new_sale = Sale(
                user_id=row['user_id'],
                product_id=row['product_id'],
                quantity=row['quantity'],
                sale_date=row['sale_date']
            )
            db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'File uploaded and data imported successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid file type.'}), 400
