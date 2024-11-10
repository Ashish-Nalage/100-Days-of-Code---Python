# Day 15 - Coffee Machine Program

## Overview
The **Coffee Machine Program** is a simulation of a coffee machine where users can select from three types of coffee: espresso, latte, and cappuccino. The machine checks if there are enough ingredients, collects payment, gives change if necessary, and updates the available resources accordingly. The game continues until the user chooses to stop or the resources run out.

## Key Features
- **Resource Management**: Tracks and updates resources such as water, milk, coffee, and money after each coffee order.
- **Payment Handling**: Collects coins from the user and ensures they pay enough for the selected coffee.
- **Sufficient Resources Check**: Verifies that there are enough resources before preparing a coffee.
- **Change Calculation**: Calculates and returns the change due to the user based on the cost of the selected coffee.
- **Report Generation**: Allows users to view the current available resources at any time.

## Program Logic
1. **Menu**:
   - The machine offers three types of coffee: espresso, latte, and cappuccino.
   - Each coffee type has a predefined set of ingredients and a cost.
2. **Check Resources**:
   - Before making coffee, the machine checks if there are enough ingredients (water, milk, coffee).
   - If any ingredient is insufficient, the user is notified and asked to select another coffee.
3. **Collect Payment**:
   - The user inserts coins (quarters, dimes, nickels, and pennies).
   - The total payment is calculated, and if it's enough to cover the cost, the coffee is made.
4. **Change Calculation**:
   - If the payment exceeds the cost of the coffee, the machine returns the change.
   - If the payment is insufficient, the transaction is canceled, and the user is refunded.
5. **Resource Update**:
   - After each coffee purchase, the machine updates its available resources and increases the money earned.
6. **Report**:
   - The user can type "report" to see the current status of available resources and the money earned.

## How to Play
1. Run the script.
2. Choose the type of coffee by typing 'espresso', 'latte', or 'cappuccino'.
3. Insert coins when prompted (quarters, dimes, nickels, pennies).
4. The machine will check if there are enough resources and whether the payment is sufficient.
5. View the available resources anytime by typing 'report'.
7. The machine terminates when you type 'off'.

## Improvements that can be done
- **More Coffee Types**: Add new types of coffee with different ingredients and costs.
- **User Authentication**: Allow users to log in and track their usage of the machine.
- **Better Payment System**: Implement a more advanced payment system with support for other currencies or digital payment methods.
- **Enhanced UI**: Create a graphical interface for a more interactive experience.

