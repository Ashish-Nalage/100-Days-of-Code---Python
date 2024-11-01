# Bill split Calculator: Splits the bill with tip among a group
print("Welcome to the Bill split Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
people = int(input("How many people to split the bill? "))

amt_per_person = round((bill + (bill * (tip / 100))) / people, 2)
print(f"Each person should pay: ${amt_per_person}")