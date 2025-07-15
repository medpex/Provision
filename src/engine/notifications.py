from flask_mail import Message
from src.app import mail

def send_new_sale_notification(sale):
    msg = Message(
        'New Sale Notification',
        sender='noreply@commission-app.com',
        recipients=[sale.user.email]
    )
    msg.body = f'Hello {sale.user.username},\n\nA new sale has been recorded for you.\n\nSale ID: {sale.id}\nProduct: {sale.product.name}\nQuantity: {sale.quantity}\nSale Date: {sale.sale_date}\n\nThank you.'
    mail.send(msg)
