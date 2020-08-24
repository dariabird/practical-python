# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows) if has_headers else []
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


if __name__ == '__main__':
    portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
    print(portfolio)
    shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
    print(shares_held)
    prices = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
    print(prices)
