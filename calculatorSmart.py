class SmartCalculator:
    """evaluates and calculates a string input with digits + - signs"""
    calc_dict = {}


    def output(self):
        while True:
            entry = input()
            #self.check_format(entry)
            if entry.startswith('/'):
                if entry == "/exit":
                    print("Bye!")
                    exit()
                elif entry == "/help":
                    print("The program calculates the sum of numbers")
                else:
                    print("Unknown command")
            elif not entry.strip():
                continue
            elif any(c.isalpha() for c in entry) is True:
                print("Invalid expression")
            elif entry.endswith('-') or entry.endswith('+') is True:
                print("Invalid expression")
            elif entry.startswith('+') is True:
                print(entry.strip('+'))
            elif '+' not in entry and '-' not in entry and entry.isdigit() is False:
                print("Invalid expression")
            elif len(entry.split()) == 1:
                print(entry)
            else:
                print(self.calculate(entry.split()))

    def calculate(self, numbers_list):
        calculation_list = self.determine_signs(numbers_list)
        result_list = []
        for i in range(0, len(calculation_list)):
            if type(calculation_list[i]) == int:
                result_list.append(calculation_list[i])
            elif calculation_list[i] == '+':
                continue
            elif calculation_list[i] == '-':
                calculation_list[i + 1] = -int(calculation_list[i + 1])
        return sum(result_list)

    def determine_signs(self, numbers_list):
        calculation_list = []
        for i in range(0, len(numbers_list)):
            try:
                calculation_list.append(int(numbers_list[i]))
            except ValueError:
                if numbers_list[i] in ['-', '+']:
                    calculation_list.append(numbers_list[i])
                else:
                    if numbers_list[i].count('-') % 2 == 1:
                        calculation_list.append('-')
                    else:
                        calculation_list.append('+')
        return calculation_list


    def check_identifier(self, entry, calc_dict):
        check_list = []
        if '=' not in entry:
            if entry.isalpha() is False:
                print("Invalid identifier")
                check_list.append(entry)
            elif entry not in calc_dict:
                print("Unknown variable")
        elif entry.count('=') == 1:
            entry2 = entry.replace(' ', '')
            entry2 = entry2.split('=')
            if entry2[0].isalpha() is False:
                print("Invalid identifier")
                check_list.append(entry)
            elif entry2[1].isdigit() is False and entry2[1].isalpha() is False:
                print("Invalid assignment")
                check_list.append(entry)
        elif entry.count('=') > 1:
            print("Invalid assignment")
            check_list.append(entry)

run = SmartCalculator()
run.output()
