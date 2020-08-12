# pcost.py
#
# Exercise 1.27 & 1.33
import csv
import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        total = 0.
        for row in rows:
            try:
                shares, price = int(row[1]), float(row[2])
                total += shares * price
            except ValueError:
                print("Couldn't parse", row)
    return total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
