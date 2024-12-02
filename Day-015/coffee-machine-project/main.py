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

def display_resources_report(resources_dict):
    """Displays a report of the current resources."""

    for key, value in resources_dict.items():
        if key in ["water", "milk"]:
            print(f"{key}: {value}ml")
        
        elif key == "coffee":
            print(f"{key}: {value}g")
        
        else:
            print(f"{key}: ${value}")


def check_resources_sufficient(coffee_name):
    """Checks if machine has sufficient ingredients for the selected coffee."""
    ingredients = MENU[coffee_name]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def update_resources(coffee_name):
    """Reduces the resources according to the selected coffee."""
    ingredients = MENU[coffee_name]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


def collect_payment():
    """Collects coins from the user and returns the total amount paid."""    
    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def calculate_change(total_amt, coffee_name):
    """Calculates the change to return to the user based on the coffee cost."""
    coffee_cost = MENU[coffee_name]["cost"]
    return round(total_amt - coffee_cost, 2)



def main():
    is_on = True
    while is_on:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        # incase user types something else 
        valid_choices = ["espresso", "latte", "cappuccino", "report", "off"]
        if coffee_type not in valid_choices:
            print("Invalid choice. Please select from espresso, latte, cappuccino, report, or off.")
            continue


        if coffee_type == "report":
            display_resources_report(resources)

        elif coffee_type == "off":
            is_on = False
        
        else:
            # Step 1: Check if resources are sufficient
            is_sufficient = check_resources_sufficient(coffee_type)
            if is_sufficient:
                # Step 2: Collect payment
                amount_paid = collect_payment()
                change_due = calculate_change(amount_paid, coffee_type)

                if change_due < 0:
                    print("Sorry that's not enough money. Money refunded.")
                    continue

                # Step 3: Update resources after a successful payment
                else:
                    update_resources(coffee_type)
                    print(f"Here is ${change_due} in change.")
                    print(f"Here is your {coffee_type} ☕️. Enjoy!")
                    resources["money"] += MENU[coffee_type]["cost"]
                    
            else:
                continue

main()