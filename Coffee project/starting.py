from data_items import MENU, resources
profit = 0


def resource_checker(items):
    for i in items:
        if items[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_coins():
    print("Enter coins")
    total = int(input("Number of quarters?: ")) * 0.25
    total += int(input("Number of dimes?: ")) * 0.10
    total += int(input("number of nickles?: ")) * 0.05
    total += int(input("Number of pennies?: ")) * 0.01
    return total


def compare(n1, n2):
    if n1 < n2:
        print(f"Sorry that's not enough money. Money Refunded.")
        return False
    elif n1 >= n2:
        change = round(n1-n2, 2)
        global profit
        profit += n2
        print(f"Here's your change {change}")
        return True


def resource_cutter(items):
    for i in items:
        resources[i] -= items[i]


is_on = True


def coffee_machine():
    while is_on:
        userChoice = input("What would you like? (espresso/latte/cappuccino): ")
        if userChoice == "off":
            break
        elif userChoice == "report":
            print(f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${profit}")
        else:
            item = MENU[userChoice]
            available = resource_checker(item["ingredients"])
            if available:
                result = process_coins()
                transaction = compare(result, item["cost"])
                if transaction:
                    resource_cutter(item["ingredients"])
                    print(f"Here is your {item}. Enjoy!")
                else:
                    coffee_machine()
            else:
                coffee_machine()


coffee_machine()