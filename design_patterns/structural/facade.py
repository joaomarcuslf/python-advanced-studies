class Discount:
    @staticmethod
    def calc(value):
        return value * 0.9


class Shipping:
    @staticmethod
    def calc():
        return 5


class Fees:
    @staticmethod
    def calc(value):
        return value * 1.5


class ShopFacade:
    def __init__(self):
        self.discount = Discount()
        self.shipping = Shipping()
        self.fees = Fees()

    def calc_price(self, price):
        price = self.discount.calc(price)
        price = self.fees.calc(price)
        price += self.shipping.calc()
        return price


""" USAGE:
facade = ShopFacade()
costs = facade.calc_price(120.25)

print(f"The Sell Cost = {costs}")
"""

""" from: https://github.com/Sean-Bradley/Design-Patterns-In-Python/blob/master/facade/shop_facade.py """
