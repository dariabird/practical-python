class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.price * self.shares

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'


class NewStock(Stock):
    def yow(self):
        print('Yow!')


if __name__ == '__main__':
    import fileparse
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    print(sum([s.cost() for s in portfolio]))

    print(NewStock.__bases__)
    print(NewStock.__mro__)
