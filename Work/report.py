# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
import sys


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        return portfolio


def read_prices(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    report = []
    for p in portfolio:
        t = (p['name'], p['shares'], p['price'], prices[p['name']]-p['price'])
        report.append(t)
    return report


def formatted_price(price):
    return f'${price:.2f}'


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print(f'{"":_>10s} {"":_>10s} {"":_>10s} {"":_>10s}')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {formatted_price(price):>10s} {change:>10.2f}')
