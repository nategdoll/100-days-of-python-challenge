from coffee_types import COFFEE_TYPES

class CoffeeMachine:
    '''
        Starts with: 
        - 300 ml of water
        - 200 ml of milk
        - 100 g of coffee
        - money from user
    '''
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.user_money = 0.0

    def report(self):
        print(f"""    Water: {self.water}ml
    Milk: {self.milk}ml
    Coffee: {self.coffee}g
    Money: ${self.user_money:.2f} """)
        
    def insert_input(self, coin_type):
        try:
            coins = int(input(coin_type))
            return coins
        except:
            print("Error amount in coins must be integer, please try again.")
            self.insert_input(coin_type)

    def coin_request(self, coffee_sel):
        price = COFFEE_TYPES[coffee_sel]["price"]
        print("Please insert coins.")
        quarters = self.insert_input("How many quarters?: ") * .25
        dimes = self.insert_input("How many dimes?: ") * .1
        nickles = self.insert_input("How many nickles?: ") * .05
        pennies = self.insert_input("How many pennies?: ") * .01
        total_change = quarters+dimes+nickles+pennies
        if price > total_change:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            self.user_money += price
            print(f"Here is ${total_change - price:.2f} in change.")
            return True

    def resource_check(self, coffee_sel):
        coffee_resources = COFFEE_TYPES[coffee_sel]
        if coffee_resources["water"] > self.water:
            print("Sorry there is not enough water.")
            return False
        elif coffee_resources["milk"] > self.milk:
            print("Sorry there is not enough milk.")
            return False
        elif coffee_resources["coffee"] > self.coffee:
            print("Sorry there is not enough coffee.")
            return False
        return True
    
    def dispense_coffee(self, coffee_sel):
        coffee_resources = COFFEE_TYPES[coffee_sel]
        self.water -= coffee_resources["water"]
        self.milk -= coffee_resources["milk"]
        self.coffee -= coffee_resources["coffee"]
        print(f"Here is your {coffee_sel} \U00002615 Enjoy!")
