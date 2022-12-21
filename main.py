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


def resources_check(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if water <= resources["water"] and coffee <= resources["coffee"]:
        if drink != "espresso":
            if MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
                resources["water"] -= water
                resources["coffee"] -= coffee
                resources["milk"] -= MENU[drink]["ingredients"]["milk"]
                return coins(drink)
            else:
                print(f"Sorry, there is not enough milk.")
        else:
            resources["water"] -= water
            resources["coffee"] -= coffee
            return coins(drink)
    elif water > resources["water"]:
        print(f"Sorry, there is not enough water.")
    elif coffee > resources["coffee"]:
        print(f"Sorry, there is not enough coffee.")
    return True


def coins(drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    cost = MENU[drink]["cost"]
    if cost <= total:
        change = float("{:.2f}".format(total - cost))
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
    else:
        print("Sorry that is not enough money. Money refunded.")
    return True


def report(resource, gain):
    for ingredient, value in resource.items():
        if ingredient == "water" or ingredient == "milk":
            print("{}:{}ml".format(ingredient.capitalize(), value))
        else:
            print("{}:{}g".format(ingredient.capitalize(), value))
    return f"Money: ${gain}"


money = 0
coffee_machine = True

while coffee_machine:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice == "report":
        print(report(resources, money))
    elif users_choice == "off":
        coffee_machine = False
        break
    else:
        resources_check(users_choice)
        money += MENU[users_choice]["cost"]




