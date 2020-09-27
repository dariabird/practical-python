# report.py
#
# Exercise 2.4
import fileparse
from portfolio import Portfolio
from stock import Stock
import tableformat


def formatted_price(price: float) -> str:
    return f'${price:.2f}'


def read_portfolio(filename, **opts):
    with open(filename, 'rt') as lines:
        return Portfolio.from_csv(lines, **opts)


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


def make_report(portfolio, prices):
    report = []
    for p in portfolio:
        t = (p.name, p.shares, p.price, prices[p.name] - p.price)
        report.append(t)
    return report


def print_report(reportdata, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    portfolio_report(portfile, pricefile, fmt)


if __name__ == '__main__':
    # import sys
    # main(sys.argv)
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv', 'txt')
