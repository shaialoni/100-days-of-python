from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()



machine_on = True

while machine_on:
    drink_order = input(f"What would you like to drink? {menu.get_items()}: ")
    drink = menu.find_drink(drink_order)
    if drink_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink_order == "off":
        machine_on = False
    elif drink_order == "cappuccino" or drink_order == "latte" or drink_order == "espresso":
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
