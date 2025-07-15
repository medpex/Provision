import datetime
from flask import make_response, Blueprint
from src.models.sale import Sale
from src.controllers.auth import commission_manager_required
import pandas as pd
from fpdf import FPDF

bp = Blueprint('reporting', __name__)

@bp.route('/report/csv', methods=['GET'])
@commission_manager_required
def export_csv(current_user):
    sales = Sale.query.all()
    df = pd.DataFrame(
        [(s.id, s.user_id, s.product_id, s.quantity, s.sale_date) for s in sales],
        columns=['id', 'user_id', 'product_id', 'quantity', 'sale_date']
    )
    output = make_response(df.to_csv())
    output.headers["Content-Disposition"] = f"attachment; filename=sales_report_{datetime.date.today()}.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@bp.route('/report/pdf', methods=['GET'])
@commission_manager_required
def export_pdf(current_user):
    sales = Sale.query.all()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sales Report", ln=1, align="C")
    for sale in sales:
        pdf.cell(200, 10, txt=f"Sale ID: {sale.id}, User ID: {sale.user_id}, Product ID: {sale.product_id}, Quantity: {sale.quantity}, Sale Date: {sale.sale_date}", ln=1)
    output = make_response(pdf.output(dest='S').encode('latin-1'))
    output.headers["Content-Disposition"] = f"attachment; filename=sales_report_{datetime.date.today()}.pdf"
    output.headers["Content-type"] = "application/pdf"
    return output
