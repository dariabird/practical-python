from report import read_portfolio
from collections import Counter


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

# The syntax is range([start,] end [,step])
for i in range(100):
    # i = 0,1,...,99
    pass
for j in range(10,20):
    # j = 10,11,..., 19
    pass
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
    pass
# The ending value is never included. It mirrors the behavior of slices.
# start is optional. Default 0.
# step is optional. Default 1.
# range() computes values as needed. It does not actually store a large range of numbers.


# The zip function takes multiple sequences and makes an iterator that combines them.
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# A common use of zip is to create key/value pairs for constructing dictionaries.
d = dict(zip(columns, values))

# Sometimes the for statement, len(), and range() get used by novices in some kind of horrible
# code fragment that looks like it emerged from the depths of a rusty C program.
data = [1, 2, 3, 4, 5]
for n in range(len(data)):
        print(data[n])
# Don’t do that! Not only does reading it make everyone’s eyes bleed,
# it’s inefficient with memory and it runs a lot slower.
# Just use a normal for loop if you want to iterate over data.
# Use enumerate() if you happen to need the index for some reason.

prices = {
    'GOOG' : 490.1,
    'AA' : 23.45,
    'IBM' : 91.1,
    'MSFT' : 34.23
}
pricelist = list(zip(prices.values(), prices.keys()))
min(pricelist)
max(pricelist)
sorted(pricelist)

a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
list(zip(a, b, c))

# Also, be aware that zip() stops once the shortest input sequence is exhausted.
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
list(zip(a,b))

# The collections module might be one of the most useful library modules for dealing with special purpose
# kinds of data handling problems such as tabulating and indexing.
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
# There are two IBM entries and two GOOG entries in this list.
# The shares need to be combined together somehow.

from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares['IBM'] )    # 150

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# Like in the previous example, the key IBM should have two different tuples instead.
# Solution: Use a defaultdict.

from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
print(holdings['IBM']) # [ (50, 91.1), (100, 45.23) ]

# Problem: We want a history of the last N things. Solution: Use a deque.
from collections import deque
history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)

holdings = Counter()
    for s in portfolio:
        holdings[s['name']] += s['shares']
    print(holdings)

    print(holdings.most_common(3))  # Get three most held stocks

    portfolio2 = read_portfolio('Data/portfolio2.csv')
    holdings2 = Counter()
    for s in portfolio2:
        holdings2[s['name']] += s['shares']
    print(holdings2)

    combined = holdings + holdings2
    print(combined)

    cost = sum([s['shares'] * s['price'] for s in portfolio])
    print(cost)
    value = sum([s['shares'] * prices[s['name']] for s in portfolio])
    print(value)

    more100 = [s for s in portfolio if s['shares'] > 100]
    print(more100)

    msftibm = [s for s in portfolio if s['name'] in {'MSFT', 'IBM'}]
    print(msftibm)

    cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000]
    print(cost10k)

    names = {s['name'] for s in portfolio}
    print(names)

    portfolio_prices = {name: prices[name] for name in names}
    print(portfolio_prices)

    f = open('Data/portfoliodate.csv')
    rows = csv.reader(f)
    headers = next(rows)
    # define a variable that lists the columns that you actually care about:
    select = ['name', 'shares', 'price']
    # Now, locate the indices of the above columns in the source CSV file:
    indices = [headers.index(colname) for colname in select]
    # Finally, read a row of data and turn it into a dictionary using a dictionary comprehension
    portfolio = [{colname: row[index] for colname, index in zip(select, indices)} for row in rows]
    print(portfolio)
    f.close()