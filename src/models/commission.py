from src.app import db

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    calculation_date = db.Column(db.DateTime, nullable=False)
    sale = db.relationship('Sale', backref=db.backref('commission', uselist=False))

    def __repr__(self):
        return f'<Commission {self.id}>'
