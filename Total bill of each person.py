# This program calculates the total bill of each person, including a tip.

print("Welcome to a Tip Calculator!")
bill = float(input("What is the total bill? "))
split = int(input("How many people are splitting the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = (bill/split) * ((1 + percentage / 100))
total_bill_rounded = round(total_bill, 2)

# This line of code rounds the number to 2 decimal places. e.g - $33.4 will become $33.40 with this line of code below
total_bill_rounded = "{:.2f}".format(total_bill)

print(f"Each person should pay ${total_bill_rounded}")
