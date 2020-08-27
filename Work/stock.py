class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.price * self.shares

    def sell(self, amount):
        self.shares -= amount


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print(s.cost())
    s.sell(25)
    print(s.shares)
    print(s.cost())
