from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

end_coffee = False
while not end_coffee:
    user_choice = input(f"​What would you like: ({menu.get_items()})? ")
    # Turn off the Coffee Machine by entering “​off​" to the prompt.
    if user_choice == 'off':
        end_coffee = True
    # print report
    elif user_choice == 'report':
        coffee.report()
        money.report()
    # make coffee
    else:
        drink = menu.find_drink(user_choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
        else:
            print('Try again later!')
    
