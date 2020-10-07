# fileparse.py
import logging


log = logging.getLogger(__name__)


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
                row = [func(val.strip('"')) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", i, row)
                    log.debug("Row %d: Reason %s", i, e)
                continue
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger('fileparse').level = logging.DEBUG
    from . import report
    a = report.read_portfolio('Data/missing.csv', silence_errors=False)

