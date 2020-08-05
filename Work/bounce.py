# bounce.py
#
# Exercise 1.5

if __name__ == "__main__":
    height = 100

    for i in range(10):
        height = height * 0.6
        print("{} {}".format(i + 1, round(height, 2)))
