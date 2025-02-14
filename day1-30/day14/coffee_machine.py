from logging import makeLogRecord
from platform import machine

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

cost = 0
starter = True
def report():
    print(f'Water : {resources['water']} ml')
    print(f'Milk : {resources['milk']} ml')
    print(f'Coffee : {resources['coffee']} gm')

def make_coffee():
    user = str(input('What would you like? (espresso/latte/cappuccino):\n')).lower()
    for key, value in MENU.items():
       if key[0] == user:
           water = value['ingredients']['water']
           coffee = value['ingredients']['coffee']
           milk = 0
           if key[0] != 'e' :
               milk = value['ingredients']['milk']
           resources_water = resources['water']
           resources_coffee = resources['coffee']
           resources_milk = resources['milk']
           if water > resources_water:
               print('Not sufficient water')
               break
           if coffee > resources_coffee:
               print('Not sufficient coffee')
               break
           if milk > resources_milk:
               print('Not sufficient milk')
               break
           else:
               global  cost
               cost += MENU['latte']['cost']
               resources['water'] -= water
               resources['coffee'] -= coffee
               resources['milk'] -= milk
               print(f'Total Cost : {cost}')

def coffee_machine():
    global starter
    ans = int(input('Welcome to coffee shop - Please select below options\n1 - Coffee report\n2 - Make Coffee\n'))
    if ans == 1:
        report()
    if ans == 2:
        while starter:
            make_coffee()

coffee_machine()
