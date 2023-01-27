from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

today_menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    item = input(f"what would you  like? {today_menu.get_items()}")
    order = today_menu.find_drink(item)

    if item == "off":
        is_on = False

    if item == "report":
        machine.report()
        money.report()

    if machine.is_resource_sufficient(order):
        print("enough resources")
    else:
        print("not enough resources")

    if money.make_payment(order.cost):
        print("enough cash")
    else:
        print("not enough cash")

    machine.make_coffee(order)
    machine.report()
    print("here's your coffee")