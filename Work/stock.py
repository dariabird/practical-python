from typedproperty import String, Integer, Float


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
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
    # import fileparse
    # with open('Data/portfolio.csv') as lines:
    #     portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    # portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    # print(sum([s.cost for s in portfolio]))
    #
    # print(NewStock.__bases__)
    # print(NewStock.__mro__)
    # s = Stock('GOOG', 100, 499.1)
    # print(s.__dict__) # 'Stock' object has no attribute '__dict__'

    x = [1, 2, 3, 4, 5]
    it = x.__iter__()
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
