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


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print(portfolio)
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)

    for r in report:
        print(r)

