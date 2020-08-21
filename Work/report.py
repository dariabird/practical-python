# report.py
#
# Exercise 2.4
import csv
from collections import Counter
from pprint import pprint
import sys


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            record = dict(zip(headers, row))
            holding = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
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
        t = (p['name'], p['shares'], p['price'], prices[p['name']] - p['price'])
        report.append(t)
    return report


def formatted_price(price):
    return f'${price:.2f}'


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    # portfolio = read_portfolio('Data/portfoliodate.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(('{:>10s} '*4).format(*headers))
    print(f'{"":_>10s} '*4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {formatted_price(price):>10s} {change:>10.2f}')

    holdings = Counter()
    for s in portfolio:
        holdings[s['name']] += s['shares']
    print(holdings)

    print(holdings.most_common(3))  # Get three most held stocks

    portfolio2 = read_portfolio('Data/portfolio2.csv')
    holdings2 = Counter()
    for s in portfolio2:
        holdings2[s['name']] += s['shares']
    print(holdings2)

    combined = holdings + holdings2
    print(combined)