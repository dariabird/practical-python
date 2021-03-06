# mortgage.py
#
# Exercise 1.7


def mortgage():
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    extra_payment_start_month = 61
    extra_payment_end_month = 108
    extra_payment = 1000.0
    month = 0

    while principal > 0:
        month = month + 1
        principal_remained = principal * (1 + rate / 12)
        if payment >= principal_remained:
            payment = principal_remained
            extra_payment = 0
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment
        # print("{} {} {}".format(month, round(total_paid, 2), round(principal, 2)))
        print(f'Months: {month}; Total Paid: {total_paid:0.2f}; Principal: {principal:0.2f}')

    # print('Total paid', round(total_paid, 2))
    print(f'Total paid: {total_paid:0.2f}')
    # print('Months', month)
    print(f'Months: {month}')


if __name__ == "__main__":
    mortgage()
