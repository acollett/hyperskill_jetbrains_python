import random
import sqlite3

class CreditCard:


    def __init__(self):
        self.iin = '400000'
        self.account_number = None
        self.checksum = None
        self.card_number = []
        self.account_numbers = []
        self.pin_code = None
        self.accounts = {}
        self.luhn_number = None

    def setup_db(self):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS card (
                            id INTEGER PRIMARY KEY,
                            number TEXT,
                            pin TEXT,
                            balance INTEGER DEFAULT 0
                        );''')
        conn.commit()


    def initial_option(self):
        self.setup_db()
        x = input(f'1. Create an account\n'
                  f'2. Log into account\n'
                  f'0. Exit\n')
        if x == '1':
            self.create_account()
        elif x == '2':
            self.login()
        elif x == '0':
            print("Bye!")
            exit()

    def create_account(self):
        random.seed()
        self.account_number = str(random.randint(100000000, 999999999))
        #while len(self.account_number) > 9:
        #    self.account_number = str(random.randint(000000000, 999999999))
        self.luhn_number = int(self.iin + self.account_number)
        luhn = [int(x) for x in str(self.luhn_number)]
        luhn2 = [x*2 for x in luhn[0:][::2]] + luhn[1:][::2]
        luhn3 = [x for x in luhn2 if x < 10] + [x-9 for x in luhn2 if x > 9]
        luhn4 = sum(luhn3) % 10
        if luhn4 == 0:
            self.checksum = '0'
        elif luhn4 > 0:
            self.checksum = str(10 - luhn4)
        self.card_number = self.iin + self.account_number + self.checksum
        self.account_numbers.append(self.card_number)
        self.pin_code = str(random.randint(1000, 9999))
        #while len(str(self.pin_code)) < 4:
        #    self.pin_code = random.randint(0000, 9999)
        self.accounts = {"Card Number": str(self.card_number),
                         "PIN code": str(self.pin_code),
                         "Balance": 0}
        # append data to db table: card
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (self.card_number, self.pin_code))
        conn.commit()
        print(f"\n"
              f"Your card has been created\n"
              f"Your card number:\n"
              f"{int(self.card_number)}\n"
              f"Your card PIN:\n"
              f"{self.pin_code}\n")
        self.option()

    def option(self):
        x = input(f''
                  f'1. Create an account\n'
                  f'2. Log into account\n'
                  f'0. Exit\n')
        if x == '1':
            self.create_account()
        elif x == '2':
            self.login()
        elif x == '0':
            print("Bye!")
            exit()

    def login(self):
        x = input("Enter your card number:\n")
        y = input("Enter you PIN:\n")
        values = self.accounts.values()
        if x in values and y in values:
            print("You have successfully logged in!")
            self.balance_option()
        else:
            print("Wrong card number or PIN!")
            self.option()

    def balance_option(self):
        x = input(f'\n'
                  f'1. Balance\n'
                  f'2. Log out\n'
                  f'0. Exit\n')
        if x == '1':
            self.show_balance()
            self.balance_option()
        elif x == '2':
            print("You have successfully logged out!")
            self.initial_option()
        elif x == '0':
            print("Bye!")
            exit()

    def show_balance(self):
        print(f'Balance: {self.accounts.get("Balance")}')

credit = CreditCard()
credit.initial_option()
