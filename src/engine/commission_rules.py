class FlatRateRule:
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, sale):
        return sale.quantity * sale.product.price * self.rate

class TieredRateRule:
    def __init__(self, tiers):
        self.tiers = tiers

    def calculate(self, sale):
        sale_amount = sale.quantity * sale.product.price
        for threshold, rate in sorted(self.tiers.items(), reverse=True):
            if sale_amount >= threshold:
                return sale_amount * rate
        return 0.0
