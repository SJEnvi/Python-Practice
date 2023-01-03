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


def print_report():
    """Prints out available resources. No input, no output"""
    for item in resources:
        print(f"There is {resources[item]} {item} remaining")
    print("And machine stores: "+str(machine_money)+"$")


def check_if_enough_resources(drink_name):
    """Takes in selected drink name and checks if there is enough resources to make it. Returns boolean"""
    # TODO make so the function iterates over the list of needed ingredients and to check if they are available
    drink = MENU[drink_name]['ingredients']
    for ingredient in drink:
        if drink[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def check_transaction(money_inserted, drink_name):
    """Takes in amount of money inserted and drink's name.
     Returns True if that's enough to buy a drink, False if not enough"""
    drink_price = MENU[drink_name]['cost']
    if money_inserted < drink_price:
        print("Sorry that's not enough money. Money refunded")
        return False
    return True


def make_drink(drink_name):
    """Takes in name of desired drink, then substracts necessary amount of resources from storage and adds drink
    cost to money stored in machine. Do not return anything"""
    drink = MENU[drink_name]
    for stored_ingredient in drink["ingredients"]:
        resources[stored_ingredient] -= drink["ingredients"][stored_ingredient]
        global machine_money
    machine_money += drink["cost"]
    print(f"Bzzz~~~... Enjoy your {drink_name}!")


def return_change(money_inserted, drink_name):
    """Takes in amout of money inserted and drink name to return float type amount of change"""
    drink_price = MENU[drink_name]['cost']
    change = money_inserted - drink_price
    return change


if __name__ == '__main__':
    machine_money = 0
    is_on = True
    make_coffee = False
    while is_on:
        user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if user_choice == 'off':
            is_on = False
        elif user_choice == 'report':
            print_report()
    # TODO Check if resources are sufficient to make coffee
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            can_make_coffee = check_if_enough_resources(user_choice)
            if can_make_coffee:
                quarters = int(input('How many quarters? : '))
                dimes = int(input('How many Dimes? : '))
                nickles = int(input('How many Nickles? : '))
                pennies = int(input('How many Pennies? : '))
                money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
                make_coffee = check_transaction(money, user_choice)
                # TODO Make coffee and tell user to enjoy his coffee
                if make_coffee:
                    make_drink(user_choice)
                    # TODO return a change to the client
                    print(f'Good choice, here is your change: ${round(return_change(money, user_choice), 2)}')
        else:
            print('This drink is not in the menu...')

