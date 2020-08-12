# pcost.py
#
# Exercise 1.27
if __name__ == "__main__":
    with open('Data/portfolio.csv', 'rt') as f:
        next(f) # to skip headers
        total = 0.
        for line in f:
            row = line.split(',')
            shares, price = int(row[1]), float(row[2])
            total += shares * price
        print("Total cost ", total)
