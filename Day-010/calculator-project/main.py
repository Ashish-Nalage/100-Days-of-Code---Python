def add(n1, n2):
    return n1 + n2   # Return the sum of two numbers
def subtract(n1, n2):
    return n1 - n2   # Return the difference
def multiply(n1, n2):
    return n1 * n2   # Return the product
def divide(n1, n2):
    return n1 / n2   # Return the quotient

# Dictionary to map operations to functions
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

from art import logo
print(logo)   # Print the calculator logo

def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))   # Get first number
    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_dictionary_key = input("Pick an operation: ")   # Choose operation
        num2 = float(input("What's the next number?: "))   # Get second number

        result = operation[operation_dictionary_key](num1, num2)   # Calculate result
        print(f"{num1} {operation_dictionary_key} {num2} = {result}")   # Display result
        
        y_or_n = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if y_or_n == "y":
            num1 = result   # Update num1 for next calculation
        else:
            should_continue = False   # End loop
            print("\n" * 100)  # Clear screen
            calculator()   # Restart calculator

calculator()   # Start the calculator