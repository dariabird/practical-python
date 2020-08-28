# pcost.py
#
# Exercise 1.27 & 1.33
import csv
import report
from stock import Stock


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0.
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost


def portfolio_cost_new(filename):
    portfolio = report.read_portfolio(filename)
    return sum(p.cost() for p in portfolio)


def main(argv):
    if len(argv) != 2:
        raise SystemExit
    portfile = argv[1]
    print('Total cost: ', portfolio_cost_new(portfile))


if __name__ == "__main__":
    import sys
    main(sys.argv)


