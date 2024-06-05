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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Check resources and deduct if available
def check_resources(item_name):
    item = MENU.get(item_name)
    if item:
        ingredients = item['ingredients']
        for ingredient, amount_needed in ingredients.items():
            if ingredient in resources and resources[ingredient] >= amount_needed:
                resources[ingredient] -= amount_needed
            else:
                print(f"Sorry, there is not enough {ingredient}")
                return False  # Resources check failed
        return True  # Resources are enough
    else:
        print("Invalid item.")
        return False

# Process payment
def payment(item_name):
    global money
    item = MENU.get(item_name)
    cost = item['cost']
    print(f"Please insert coins. Cost: ${cost}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if total_money < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False  # Payment failed
    else:
        change = round(total_money - cost, 2)
        money += cost  # Update money only if payment is successful
        print(f"Here is ${change} in change. Thank you.")
        return True  # Payment successful

end_of_coffee = False
while not end_of_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino/):").lower()
    if user_choice == 'off':
        end_of_coffee = True
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_choice in MENU:
        if check_resources(user_choice) and payment(user_choice):
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print('Try again later!')
    else:
        end_of_coffee = True

