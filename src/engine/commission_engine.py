class CommissionEngine:
    def __init__(self, rules):
        self.rules = rules

    def calculate(self, sale):
        for rule in self.rules:
            commission = rule.calculate(sale)
            if commission is not None:
                return commission
        return 0.0
