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

    '''
    Format codes (after the : inside the {}) are similar to C printf(). Common codes include:
    d       Decimal integer
    b       Binary integer
    x       Hexadecimal integer
    f       Float as [-]m.dddddd
    e       Float as [-]m.dddddde+-xx
    g       Float, but selective use of E notation
    s       String
    c       Character (from integer)
    
    :>10d   Integer right aligned in 10-character field
    :<10d   Integer left aligned in 10-character field
    :^10d   Integer centered in 10-character field
    :0.2f   Float with 2 digit precision
    '''
    '{:10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
    print('%5d %-5d %10d' % (3, 4, 5))
    # Note: This is the only formatting available on byte strings.
    print(b'%s has %n messages' % (b'Dave', 37))
