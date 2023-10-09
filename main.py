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

gains = 0


def report():
    string = ""
    global gains, resources
    for key in resources:
        string += f"{key} : {resources[key]}\n"
    string += f"money : {gains}JD"
    return string


def get_coins():
    half = int(input("how many half jds? ")) * 0.5
    quarter = int(input("how many quarters? ")) * 0.25
    ten_cents = int(input("how many ten_cents? ")) * 0.1
    five_cents = int(input("how many five_cents? ")) * 0.05
    return half, quarter, ten_cents, five_cents


def is_sufficient_ingredients(drink, res):
    global MENU
    flag = True
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > res[key]:
            flag = False
    return flag


def make_drink(drink):
    global MENU, resources, total, gains
    if is_sufficient_ingredients(drink, resources):
        for key in MENU[drink]["ingredients"]:
            resources[key] -= MENU[drink]["ingredients"][key]
        print(f'here is your change: {total - MENU[drink]["cost"]}')
        print(f"Here is ur {drink} enjoy!")
        gains +=  MENU[drink]["cost"]
    else:
        print("insufficient ingredients sorry!")


total = 0
while True:
    choice = input("what would u like? (latte,espresso,cappuccino)? ").lower()
    if choice == "report":
        print(report())
    elif choice == 'exit':
        break
    else:
        drink = MENU[choice]
        print(f"that will cost you {drink['cost']}")
        print("please insert coins.")
        half, quarter, ten_cents, five_cents = get_coins()
        total = half + quarter + ten_cents + five_cents
        if total >= MENU[choice]["cost"]:
            make_drink(choice)
        else:
            print("sorry thats insufficient, your money is refunded")
