# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(iterable, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse iterable into a list of records
    '''
    if isinstance(iterable, str):
        raise ValueError("Parameter 'iterable' must be a file-like/iterable object")
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    rows = [row.strip().split(delimiter) for row in iterable]

    # Read the file headers
    headers = rows[0] if has_headers else []
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
        if has_headers and i == 1:
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
    lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
    port = parse_csv(lines, types=[str, int, float])
    print(port)
    import gzip
    with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
        port = parse_csv(file, types=[str, int, float])
    print(port)
