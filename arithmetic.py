import random


class ArithmeticExam:

    def __init__(self):
        self.enter = ''
        self.answer = int
        self.mark = []
        self.level = []
        self.description = ""

    def choose_level(self):
        self.level = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
''')
        if self.level == "1":
            self.description = "1 - simple operations with numbers 2-9"
            self.run1()
        elif self.level == "2":
            self.description = "2 - integral squares of 11-29"
            self.run2()
        else:
            print('Incorrect format.')
            self.choose_level()
        self.save_result()

    def rand_question(self):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        seq = ['+', '-', '*']
        sign = random.choice(seq)
        self.question = str(a) + ' ' + str(sign) + ' ' + str(b)
        print(self.question)
        return self.question

    def square_question(self):
        c = random.randint(11, 29)
        self.square_ans = c * c
        print(c)
        return self.square_ans

    def response(self):
        enter = input()
        try:
            enter = int(enter)
        except ValueError:
            if enter.isdigit() is False:
                print("Incorrect format.")
                self.response()
        else:
            x = self.question.split(" ")
            if x[1] == '+':
                self.answer = int(x[0]) + int(x[2])
            elif x[1] == '*':
                self.answer = int(x[0]) * int(x[2])
            elif x[1] == '-':
                self.answer = int(x[0]) - int(x[2])
            if enter == self.answer:
                print("Right!")
                self.mark.append(self.answer)
            else:
                print("Wrong!")

    def response2(self):
        enter = input()
        try:
            enter = int(enter)
        except ValueError:
            if enter.isdigit() is False:
                print("Incorrect format.")
                self.response2()
        else:
            if enter == self.square_ans:
                print("Right!")
                self.mark.append(self.square_ans)
            else:
                print("Wrong!")

    def save_result(self):
        enter = input('''Would you like to save your result to the file? "
Enter yes or no.
''')
        yes = ['yes', 'YES', 'y', 'Yes']
        if enter in yes:
            name = input("What is your name?\n")
            record = f"{name}: {len(self.mark)}/5 in level {self.description}"
            f = open("results.txt", 'a')
            f.write(record)
            f.close()
            print(f'The results are saved in "results.txt"')
        else:
            exit()

    def run1(self):
        n = 0
        while n < 5:
            self.rand_question()
            self.response()
            n = n + 1
        print(f"Your mark is {len(self.mark)}/5")

    def run2(self):
        n = 0
        while n < 5:
            self.square_question()
            self.response2()
            n = n + 1
        print(f"Your mark is {len(self.mark)}/5")

Test = ArithmeticExam()
Test.choose_level()
