OFF = False
ON = True
MONEY = 0.00

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

def check_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for item, amount_needed in ingredients.items():
        if amount_needed > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make(coffee):        
    ingredients = MENU[coffee]["ingredients"]
    for item, amount_needed in ingredients.items():
        resources[item] -= amount_needed
    return print(f"Here is your {coffee}. Enjoy!")

def money(coffee):
    global MONEY
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    needed_amount = MENU[coffee]["cost"]
    total = round(quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01, 2)
    if total < needed_amount:
        return False
    else:
        MONEY += needed_amount
        change = round(total - needed_amount, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True


def check():
    print(f"Water: {resources["water"]}ml ")
    print(f"Milk: {resources["milk"]}ml ")
    print(f"Coffee: {resources["coffee"]}g ")
    print(f"Money: ${MONEY:.2f}")
    
def machine():
    status = ON
    while status == ON:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            status = OFF
        elif user_input == "report":
            check()
        elif user_input in MENU:
            if check_resources(user_input):
                if money(user_input):
                    make(user_input)  
                else:
                    print("Sorry that's not enough money. Money refunded.")  
        else:
            print("Invalid choice, please try again.")


machine()