Money = 0.0
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


def coffee_machine():
    global Money
    # TODO : 1.Print out all coffee machine resources.
    # print(f"Coffee machine resources:\n Water: ", resources["water"], "\n Milk:", resources["milk"], "\n Coffee:",
    # resources["coffee"])

    # TODO: 2. ask the user what they would like to do.

    order = input("What would you like to order? (espresso/ latte/ cappuccino)")

    # TODO: 3. allow ability to turn off the machine

    if order == "off":
        exit()

    # TODO: 4. if the user enters report then print out the report
    if order == "report":
        print(f"Coffee machine resources:\n Water: ", resources["water"], "\n Milk:", resources["milk"], "\n Coffee:",
              resources["coffee"], f"\n Money: {Money} $")

    # TODO: 5. Check if there are sufficient resources to complete the order
    if order == "espresso":
        if MENU["espresso"]["ingredients"]["water"] < resources["water"] and MENU["espresso"]["ingredients"]["coffee"] < \
                resources["coffee"]:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            Money = Money + MENU["espresso"]["cost"]
            payment = float(input("The cost of this item is 1.50$ .How much would you like to pay?"))
            if payment >= float(MENU["espresso"]["cost"]):
                print("Here is your espresso, enjoy.")
                if payment > int(MENU["espresso"]["cost"]):
                    change = payment - float(MENU["espresso"]["cost"])
                    print(f"Here is your change: {change}$")

            coffee_machine()
        else:
            print("Your order has been declined")
            coffee_machine()
    elif order == "latte":
        if MENU["latte"]["ingredients"]["water"] < resources["water"] and MENU["latte"]["ingredients"]["coffee"] < \
                resources["coffee"] and MENU["latte"]["ingredients"]["milk"] < resources["milk"]:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            Money = Money + MENU["latte"]["cost"]
            payment = float(input("The cost of this item is 2.50$ .How much would you like to pay?"))
            if payment >= float(MENU["latte"]["cost"]):
                print("Here is your Latte,enjoy.")
                if payment > int(MENU["latte"]["cost"]):
                    change = payment - float(MENU["latte"]["cost"])
                    print(f"Here is your change: {change}$")

            coffee_machine()
        else:
            print("Sorry your order has been declined due to lack of resources.")
            coffee_machine()
    elif order == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] < resources["water"] and MENU["cappuccino"]["ingredients"][
            "coffee"] < \
                resources["coffee"] and MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            Money = Money + MENU["cappuccino"]["cost"]
            payment = float(input("The cost of this item is 3.00$ .How much would you like to pay?"))
            if payment >= float(MENU["cappuccino"]["cost"]):
                print("Here is your cappuccino, enjoy!")
                if payment > int(MENU["cappuccino"]["cost"]):
                    change = payment - float(MENU["cappuccino"]["cost"])
                    print(f"Here is your change: {change}$")
            coffee_machine()
        else:
            print("Sorry your order has been declined due to lack of resources.")
            coffee_machine()
    else:

        coffee_machine()
    # TODO 6: process the payment they the customer inputs


coffee_machine()
