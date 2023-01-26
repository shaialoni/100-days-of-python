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
machine_on = True


def accept_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins")
    cash = int(input("How many quarters?: ")) * 0.25
    cash += int(input("How many dimes?: ")) * 0.1
    cash += int(input("How many nickels?: ")) * 0.05
    cash += int(input("How many pennies?: ")) * 0.01
    return cash


def check_resources(selection):
    """ This function takes in a string of coffee selection and return True / False based on availability of
    ingredients"""
    for item in MENU[selection]["ingredients"]:
        # print(f"in menu {item}", MENU[selection]["ingredients"][item])
        # print(f"in resources {item}", resources[item])
        if resources[item] < MENU[selection]["ingredients"][item]:
            print(f"Sorry, but there is not enough {item} to complete your request")
            return False

        return True


def use_resources(selection):
    """This function takes the coffee selection and reduces the appropriate resources from the resource dict, according
    to resources needed from MENU"""
    for item in MENU[selection]["ingredients"]:
        # print(f"in menu {item}", MENU[selection]["ingredients"][item])
        # print(f"in resources {item}", resources[item])
        resources[item] -= MENU[selection]["ingredients"][item]


while machine_on:
    coffee_selection: str = input("What type of coffee would you like? (espresso/latte/cappuccino): ")
    if coffee_selection == "report":
        if len(resources) == 4:
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']} ")
        else:
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    elif coffee_selection == "off":
        machine_on = False
    elif coffee_selection == "espresso" or coffee_selection == "cappuccino" or coffee_selection == "latte":
        if check_resources(coffee_selection):
            cash_in = accept_coins()
            cash_in -= MENU[coffee_selection]["cost"]
            cash_in = round(cash_in, 2)
            if cash_in >= 0:
                print(f"Here is {cash_in} in change.")
                print(f"Here is your {coffee_selection},. Enjoy!")
                use_resources(coffee_selection)
                if len(resources) == 3:
                    resources["money"] = MENU[coffee_selection]["cost"]
                else:
                    resources["money"] += MENU[coffee_selection]["cost"]
            else:
                cash_in = cash_in + MENU[coffee_selection]['cost']
                cash_in = round(cash_in, 2)
                print(f"Sorry, this is not enough money, a {coffee_selection} is ${MENU[coffee_selection]['cost']}")
                print(f"{cash_in} refunded.")

            # print("chaching", resources)
