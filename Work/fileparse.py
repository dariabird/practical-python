# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

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
        for i, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {i}: {row} Error: {e}')
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


if __name__ == '__main__':
    # portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
    # print(portfolio)
    # shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
    # print(shares_held)
    # prices = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
    # print(prices)
    # portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
    # print(portfolio)
    portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
    print(portfolio)
