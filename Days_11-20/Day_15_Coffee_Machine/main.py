from coffee_machine import CoffeeMachine

def make_selection():
    selection = None

    while selection is None:
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection not in ('report', 'off', 'espresso', 'latte', 'cappuccino'):
            print("I'm sorry I didn't recognize your selection please try again.")
            selection = None
    
    return selection
    
def main():
    coffeemaker = CoffeeMachine()
    selection = 'on'
    while selection != 'off':
        selection = make_selection()
        if selection == 'report':
            coffeemaker.report()
        elif selection == 'off':
            pass
        else:
            if coffeemaker.resource_check(selection):
                if coffeemaker.coin_request(selection):
                    coffeemaker.dispense_coffee(selection)
    print("Coffee maker is off time to call it quits for the day.")

main()