# report.py
#
# Exercise 2.4
import fileparse
import csv


def formatted_price(price: float) -> str:
    return f'${price:.2f}'


def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as f:
        return fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename: str) -> dict:
    with open(filename, 'rt') as f:
        rows = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    prices = {}
    for row in rows:
        try:
            prices[row[0]] = row[1]
        except IndexError:
            pass
    return prices


def make_report(portfolio: list, prices: list) -> list:
    report = []
    for p in portfolio:
        t = (p['name'], p['shares'], p['price'], prices[p['name']] - p['price'])
        report.append(t)
    return report


def print_report(report: list):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(('{:>10s} ' * 4).format(*headers))
    print(f'{"":_>10s} ' * 4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {formatted_price(price):>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename: str, prices_filename: str):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys
    main(sys.argv)



