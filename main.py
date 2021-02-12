MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO : 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
# TODO : 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO:  3. Print report.
# TODO:  4. Check resources sufficient?
# TODO:  5. Process coins.
# TODO:  6. Check transaction successful?
# TODO:  7. Make Coffee.

money = 0


def report():
    print(f"Water: {resources['water']}ml ")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def make_espresso():
    global money

    if (resources['water'] >= MENU['espresso']['ingredients']['water'] and
            resources['coffee'] >= MENU['espresso']['ingredients']['coffee']):
        print("Please insert coins")
        quarters = int(input("How many quarters ?: "))
        dimes = int(input("How many dimes ?: "))
        nickles = int(input("How many nickles ?: "))
        pennies = int(input("How many pennies ?: "))

        total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if total < MENU['espresso']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:

            if total > MENU['espresso']['cost']:
                change = total - MENU['espresso']['cost']
                print(f"Here is {round(change,2)} in change")

                money += MENU['espresso']['cost']

                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']

                print("Here is your espresso ☕️. Enjoy!")

    elif resources['water'] < MENU['espresso']['ingredients']['water']:
        print("Sorry there is not enough water.")

    else:
        print("Sorry there is not enough coffee.")


def make_latte():
    global money

    if (resources['water'] >= MENU['latte']['ingredients']['water']
            and resources['coffee'] >= MENU['latte']['ingredients']['coffee']
            and resources['milk'] > MENU['latte']['ingredients']['milk']):

        print("Please insert coins")
        quarters = int(input("How many quarters ?: "))
        dimes = int(input("How many dimes ?: "))
        nickles = int(input("How many nickles ?: "))
        pennies = int(input("How many pennies ?: "))

        total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if total < MENU['latte']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:

            if total > MENU['latte']['cost']:
                change = total - MENU['latte']['cost']
                print(f"Here is {round(change, 2)} in change")

            money += MENU['latte']['cost']

            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            resources['milk'] -= MENU['latte']['ingredients']['milk']

            print("Here is your latte ☕️. Enjoy!")

    elif resources['water'] < MENU['latte']['ingredients']['water']:
        print("Sorry there is not enough water.")

    elif resources['milk'] < MENU['latte']['ingredients']['milk']:
        print("Sorry there is not enough milk.")

    else:
        print("Sorry there is not enough coffee.")


def make_cappuccino():
    global money

    if (resources['water'] >= MENU['cappuccino']['ingredients']['water']
            and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']
            and resources['milk'] > MENU['cappuccino']['ingredients']['milk']):

        print("Please insert coins")
        quarters = int(input("How many quarters ?: "))
        dimes = int(input("How many dimes ?: "))
        nickles = int(input("How many nickles ?: "))
        pennies = int(input("How many pennies ?: "))

        total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if total < MENU['cappuccino']['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:

            if total > MENU['cappuccino']['cost']:
                change = total - MENU['cappuccino']['cost']
                print(f"Here is {round(change, 2)} in change")

            money += MENU['cappuccino']['cost']

            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']

            print("Here is your cappuccino ☕️. Enjoy!")

    elif resources['water'] < MENU['cappuccino']['ingredients']['water']:
        print("Sorry there is not enough water.")

    elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
        print("Sorry there is not enough milk.")

    else:
        print("Sorry there is not enough coffee.")

is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        report()
    elif user_input == "espresso":
        make_espresso()
    elif user_input == "latte":
        make_latte()
    elif user_input == "cappuccino":
        make_cappuccino()
    elif user_input == "off":
        is_on = False




