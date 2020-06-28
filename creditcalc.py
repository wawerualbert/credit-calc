
import argparse
from math import ceil, log


def format_months(months):
    years_str = months_str = separator = ''
    years = months // 12
    months = months % 12
    if years != 0:
        years_str += f'{years} year'
        if years != 1:
            years_str += 's'
    if months != 0:
        months_str += f'{months} month'
        if months != 1:
            months_str += 's'
    if not(months == 0 or years == 0):
        separator += ' and '

    return years_str + separator + months_str


def calc_months(principal, monthly_payment, interest):
    months = ceil(log(monthly_payment / (monthly_payment - interest * principal), 1 + interest))
    print(f' You need {format_months(months)} to repay this credit!')
    overpayment = principal - monthly_payment * months
    print(f'Overpayment = {overpayment}')


def calc_annuity(principal, months, interest):
    annuity = ceil(principal * (interest * pow(1 + interest, months) / (pow(1 + interest, months) - 1)))
    print(f'Your annuity payment = {annuity}!')
    overpayment = principal - annuity * months
    print(f'Overpayment = {overpayment}')


def calc_principal(monthly_payment, months, interest):
    principal = ceil(monthly_payment / (interest * pow(1 + interest, months) / (pow(1 + interest, months) - 1)))
    print(f'Your credit principal = {principal}!')
    overpayment = principal - monthly_payment * months
    print(f'Overpayment = {overpayment}')


def calc_differentiated_payments(principal, months, interest):
    total_payment = 0
    for month in range(1, months + 1):
        payment = ceil(principal / months + interest * (principal - (principal * (month - 1)) / months))
        total_payment += payment
        print(f'Month {month}: {payment}')
    overpayment = principal - total_payment
    print(f'Overpayment = {overpayment}')


def correct_args(principal, payment, periods, interest):
    sum_ = 0
    if principal is not None:
        sum_ += 1
    if payment is not None:
        sum_ += 1
    if periods is not None:
        sum_ += 1
    if interest is not None:
        sum_ += 1
    if sum_ < 3:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str)
    parser.add_argument('--principal', type=int)
    parser.add_argument('--payment', type=int)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    args = parser.parse_args()

    if not correct_args(args.principal, args.payment, args.periods, args.interest):
        print('Incorrect parameters')
    elif args.type != 'diff' and args.type != 'annuity' or args.type is None:
        print('Incorrect parameters')
    elif args.type == 'diff':
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            calc_differentiated_payments(args.principal, args.periods, args.interest / 1200)
    else:
        if args.principal is None:
            if args.payment < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_principal(args.payment, args.periods, args.interest / 1200)
        elif args.payment is None:
            if args.principal < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_annuity(args.principal, args.periods, args.interest / 1200)
        elif args.periods is None:
            if args.principal < 0 or args.payment < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_months(args.principal, args.payment, args.interest / 1200)

main()
