class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f'Water : {self.resources['water']} ml')
        print(f'Milk : {self.resources['milk']} ml')
        print(f'Coffee : {self.resources['coffee']} gm')

    def is_resources_available(self,drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f'Sorry there is not enough{item}')
                return False                    
        return True
    def make_drink(self,order):
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f'Here is your drink {order.name} ! Enjoy ☕️')    


        





                