print("\n======================================")
print("Welcome to the Tip Calculator!")
print("======================================\n")

total = float(input("What was the total bill? \n$"))
tip = int(input("\nWhat percentage tip would you like to give? 10, 12 or 15?\n$"))
people = int(input("\nHow many people to split the bill?\n"))
bill = round((total+(total*(tip/100)))/people,2)

print("\n-------------------------------------------")
print(f"\nEach person sould pay: ${bill}")
print("\n-------------------------------------------\n")

input("\nPress Enter to exit...")