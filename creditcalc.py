import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates stuff")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help="you need to choose annuity of diff")
parser.add_argument("--payment", help="use with --type=diff NOT annunity",
                    type=int)  # use with --type=diff
parser.add_argument("--principal", type=int)  # use with both types
parser.add_argument("--periods", type=int)  #
parser.add_argument("--interest", type=float)  # must be provided, can be float

args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters")
# calculates diff or annuity depending on user input
elif args.type == "diff" and args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is True:
    print("Incorrect parameters")
elif args.type == "diff":
    i = args.interest / (100 * 12)
    m = 0  # month of the diff calc starting at 1
    diff_list = []
    while m < args.periods:
        m = m + 1
        diff = (args.principal / args.periods) + i * \
               (args.principal - ((args.principal * (m - 1)) / args.periods))
        print(f"Month {m}: payment is {math.ceil(diff)}")
        diff_list.append(math.ceil(diff))
    overpayment = sum(diff_list) - args.principal
    print(f"\nOverpayment = {overpayment}")

elif args.type == "annuity":  # and args.interest is True:
    if args.periods is None:
        i = args.interest / 12 / 100
        x = (args.payment / (args.payment - i * args.principal))
        base = 1 + i
        no_of_months = math.log(x, base)
        years_months = divmod(math.ceil(no_of_months), 12)

        if years_months[0] == 0 and years_months[1] == 1:
            print("It will take 1 month to repay the loan!")
        elif years_months[0] == 1 and years_months[1] == 0:
            print("It will take 1 year to repay the loan!")
        elif years_months[0] > 1 and years_months[1] == 1:
            print("It will take", years_months[0], "years and 1 month to repay the loan!")
        elif years_months[0] > 1 and years_months[1] == 0:
            print("It will take", years_months[0], "years to repay the loan!")
        elif years_months[0] == 0 and years_months[1] > 1:
            print("It will take and", years_months[1], "months to repay the loan!")
        elif years_months[0] == 1 and years_months[1] > 1:
            print("It will take 1 year and", years_months[1], "months to repay the loan!")
        else:
            print("It will take", years_months[0], "years and", years_months[1], "months to repay the loan!")
        # overpayment calc
        overpayment = args.payment * math.ceil(no_of_months) - args.principal
        print(f"Overpayment = {overpayment}")

    elif args.payment is None:  # calc_what == "a":
        i = args.interest / 12 / 100
        payment = args.principal * ((i * math.pow(1 + i, args.periods)) /
                                    (math.pow(1 + i, args.periods) - 1))
        print(f"Your annuity payment = {math.ceil(payment)}!")

    elif args.principal is None:  # calc_what == "p":
        i = args.interest / 12 / 100
        principal = args.payment / ((i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1))
        print(f"Your loan principal = {round(principal)}!")
    else:
        print("Error restart program")
else:
    print("Incorrect parameters")
