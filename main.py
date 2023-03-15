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
    "money": 0
}


def report():
    print(resources)


def check_resources(coffe_type):

    if coffe_type not in MENU:
        raise Exception("Invalid selection")

    for ingredient in MENU[coffe_type]["ingredients"]:
        if resources[ingredient] < MENU[coffe_type]["ingredients"][ingredient]:
            raise Exception("Error. Insufficient " + ingredient + " for your " + coffe_type + ". Required: " +
                            str(MENU[coffe_type]["ingredients"][ingredient]) + ". Available "
                            + str(resources[ingredient]))


def payout(coffe_type):
    cents = int(input("Amount of cents coins\n"))
    five_cents = int(input("Amount of 5 cents coins\n"))
    ten_cents = int(input("Amount of 10 cents coins\n"))
    twenty_five_cents = int(input("Amount of 25 cents coins\n"))

    amount = (cents + (five_cents * 5) + (ten_cents * 10) + (twenty_five_cents * 25)) / 100.0
    if amount < MENU[coffe_type]["cost"]:
        raise Exception("Insufficient funds. You entered " + str(amount) + " €. Required for " + coffe_type
                        + " is " + str(MENU[coffe_type]["cost"]) + "€")
    print("Your input: " + "{:.2f}€".format(amount))
    print(coffe_type + " price: " + "{:.2f}€".format(MENU[coffe_type]["cost"]))
    exchange = amount - MENU[coffe_type]["cost"]
    print("Your change: " + "{:.2f}€".format(exchange))

    confirm_transaction(coffe_type)

    print("Your " + coffe_type + " is ready...")


def confirm_transaction(coffe_type):
    for ingredient in MENU[coffe_type]["ingredients"]:
        resources[ingredient] -= MENU[coffe_type]["ingredients"][ingredient]

    if "money" in resources:
        resources["money"] += MENU[coffe_type]["cost"]


user_option = ""

while True:
    print("Coffe machine ☕. What do you want?")
    user_option = input("Espresso/Latte/Cappuccino\n").lower()
    if user_option.lower() == "off":
        break
    elif user_option.lower() == "report":
        report()
    else:
        try:
            check_resources(user_option)
            payout(user_option)
        except Exception as err:
            print(err)


print("Bye bye")
