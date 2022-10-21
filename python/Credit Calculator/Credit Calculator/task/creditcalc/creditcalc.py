#!/usr/bin/python3
import math
import argparse


def count_of_months(p, a, i):
    # p: principal a: monthly payment i: interest rate
    i = i / 1200
    n = math.ceil(math.log(a / (a - i * p), 1 + i))
    if n == 1:
        return 'You need {} month to repay this credit!\nOverpayment = {}'.format(n, a * n - p)
    if 1 < n < 12:
        return 'You need {} months to repay this credit!\nOverpayment = {}'.format(n, a * n - p)
    elif n == 12:
        return 'You need 1 year to repay this credit!\nOverpayment = {}'.format(a * 12 - p)
    elif 12 < n < 24:
        if n % 12 == 1:
            return 'You need {} year and 1 month to repay this credit!\nOverpayment = {}'.format(math.floor(n / 12),
                                                                                                 a * n - p)
        else:
            return 'You need {} year and {} months to repay this credit!\nOverpayment = {}'.format(math.floor(n / 12),
                                                                                                   n % 12, a * n - p)
    elif n >= 24:
        if n % 12 == 0:
            return 'You need {} years to repay this credit!\nOverpayment = {}'.format(math.floor(n / 12), a * n - p)
        elif n % 12 == 1:
            return 'You need {} years and 1 month to repay this credit!\nOverpayment = {}'.format(math.floor(n / 12),
                                                                                                  a * n - p)
        else:
            return 'You need {} year and {} months to repay this credit!\nOverpayment = {}'.format(math.floor(n / 12),
                                                                                                   n % 12, a * n - p)


def annuity_monthly_payment(p, n, i):
    # p: principal n: period i: interest in percentage per month
    i = i / 1200
    result = math.ceil(p * i * pow(1 + i, n) / (pow(1 + i, n) - 1))
    return 'Your annuity payment = {}!\nOverpayment = {}'.format(result, result * n - p)


def credit_principal(a, n, i):
    # a: monthly payment n: periods i: interest
    i = i / 1200
    result = a * (pow(1 + i, n) - 1) / (i * pow(1 + i, n))
    return 'Your credit principal = {}!\nOverpayment = {}'.format(result, a * n - result)


def diff(p, n, i):
    i = i / 1200
    overpayment = - p
    for m in range(1, n + 1):
        result = math.ceil(p / n + i * (p - (p * m - p) / n))
        print('Month {}: paid out {}'.format(m, result))
        overpayment += result
    print('')
    print(f'Overpayment = {overpayment}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--type')
    ap.add_argument('--payment')
    ap.add_argument('--principal')
    ap.add_argument('--periods')
    ap.add_argument('--interest')
    args = vars(ap.parse_args())
    if args['type'] == 'annuity' and args['interest'] is not None:
        i = float(args['interest'])
        if args['payment'] is None:
            p = int(args['principal'])
            n = int(args['periods'])
            print(annuity_monthly_payment(p, n, i))
        elif args['principal'] is None:
            a = float(args['payment'])
            n = int(args['periods'])
            print(credit_principal(a, n, i))
        elif args['periods'] is None:
            print(args)
            p = int(args['principal'])
            a = float(args['payment'])
            print(count_of_months(p, a, i))
    elif args['type'] == 'diff' and args['interest'] is not None:
        i = float(args['interest'])
        p = int(args['principal'])
        n = int(args['periods'])
        diff(p, n, i)
    else:
        print('Incorrect parameters')


if __name__ == '__main__':
    main()
