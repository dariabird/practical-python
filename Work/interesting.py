if __name__ == "__main__":
    s = 'hello'
    '''
    dir() produces a list of all operations that can appear after the (.).
    '''
    print(dir(s))
    '''
    Use the help() command to get more information about a specific operation
    '''
    help(s.upper)

    '''
    If the element is present more than once, index() will return the index of the first occurrence.
    If the element is not found, it will raise a ValueError exception.
    '''
    names = ['Elwood','Jake','Curtis']
    names.index('Curtis')

    # Using the value
    names.remove('Curtis')

    # Using the index
    del names[1]

    # in-place sorting
    s = [10, 1, 7, 3]
    s.sort()  # [1, 3, 7, 10]

    # Reverse order
    s = [10, 1, 7, 3]
    s.sort(reverse=True)  # [10, 7, 3, 1]

    # It works with any ordered data
    s = ['foo', 'bar', 'spam']
    s.sort()  # ['bar', 'foo', 'spam']
    t = sorted(s)  # s unchanged, t holds sorted values

    import gzip
    # Including the file mode of 'rt' is critical here.
    # If you forget that, you’ll get byte strings instead of normal text strings.
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')

    import csv
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        print(row)

    s = {
        'name': 'GOOG',
        'shares': 100,
        'price': 490.1
    }
    # To delete a value use the del statement.
    del s['date']

    # You can look up a value that might not exist and provide a default value in case it doesn’t.
    # name = d.get(key, default)

    prices = {}  # Initial empty dict

    # Insert new items
    prices['GOOG'] = 513.25
    prices['CAT'] = 87.22
    prices['IBM'] = 93.37

    prices.get('IBM', 0.0)
    prices.get('SCOX', 0.0)
