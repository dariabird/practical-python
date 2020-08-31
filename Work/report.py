# report.py
#
# Exercise 2.4
import fileparse
from stock import Stock
import tableformat


def formatted_price(price: float) -> str:
    return f'${price:.2f}'


def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    return [Stock(d['name'], d['shares'], d['price']) for d in portfolio]


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
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print(('{:>10s} ' * 4).format(*headers))
    # print(f'{"":_>10s} ' * 4)
    # for name, shares, price, change in report:
    #     print(f'{name:>10s} {shares:>10d} {formatted_price(price):>10s} {change:>10.2f}')


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
    if len(argv) != 3:
        raise SystemExit
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys
    main(sys.argv)


