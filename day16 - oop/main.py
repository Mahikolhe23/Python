from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_machine_on = True

while is_machine_on:
    order = str(input(f'What would you like? {menu.get_items()}')).lower()
    order = menu.find_drink(order)
    if coffee.is_resources_available(order) and money.make_payment(order.cost):
        coffee.make_drink(order)
