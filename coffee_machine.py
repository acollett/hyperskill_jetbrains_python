class CoffeeMachine:
    choice = ['espresso', 'latte', 'cappuccino']
    consumption = [[-250, -0, -16, -1, 4], [-350, -75, -20, -1, 7], [-200, -100, -12, -1, 6]]
    supplies = ['water', 'milk', 'coffee beans', 'cups']

    def __init__(self):
        self.resources = [400, 540, 120, 9, 550]
        self.state = 'Main'

    def __str__(self):
        return f""

    def machine_resources(self):
        print(f'''The coffee machine has:
        {self.resources[0]} of water
        {self.resources[1]} of milk
        {self.resources[2]} of coffee beans
        {self.resources[3]} of disposable cups
        ${self.resources[4]} of money\n''')
        return

    def menu(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        self.state = action
        return action

    def menu_option(self):
        loop = True
        while loop:
            if self.state == 'Main':
                self.menu()
            elif self.state == 'buy':
                self.buy()
                self.state = 'Main'
            elif self.state == 'fill':
                self.fill()
                self.state = 'Main'
            elif self.state == 'take':
                self.take()
                self.state = 'Main'
            elif self.state == 'remaining':
                self.state = 'Main'
                self.machine_resources()
            elif self.state == 'exit':
                exit()
                loop = False
        return

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        # supplies = ['water', 'milk', 'coffee beans', 'cups']
        if coffee_type == 'back':
            self.state = 'Main'
            self.menu_option()
        else:
            for i in range(4):
                if self.resources[i] + CoffeeMachine.consumption[int(coffee_type) - 1][i] < 0:
                    print(f"Sorry, not enough {CoffeeMachine.supplies[i]}!")
                    self.state = 'Main'
                    self.menu_option()
                else:
                    continue
            for i in range(5):
                self.resources[i] += CoffeeMachine.consumption[int(coffee_type) - 1][i]
            print("I have enough resources, making you a coffee!")
            return self.resources

    def fill(self):
        self.resources[0] += int(input("Write how many ml of water do you want to add:\n"))
        self.resources[1] += int(input("Write how many ml of milk do you want to add:\n"))
        self.resources[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.resources[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        return self.resources

    def take(self):
        print(f"I gave you ${self.resources[4]}\n")
        self.resources[4] = 0
        return

run = CoffeeMachine()
run.menu_option()
