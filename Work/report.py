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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio = read_portfolio(filename)
    total = 0.
    for s in portfolio:
        total += s['shares'] * s['price']

    prices = read_prices('Data/prices.csv')

    gain_loss = 0.
    for p in portfolio:
        if p['name'] in prices:
            gain_loss += (p['price'] - prices[p['name']]) * p['shares']
    print(gain_loss)


