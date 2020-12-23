# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like togive? 10, 12 or 15?")
split = input("How many people to split the bill?")
each_to_give = round(((float(bill) + ((int(tip) / 100) * float(bill))) / int(split)), 2)
print(f"Each person should pay: ${each_to_give}")
