print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15"))
number_people = int(input("How many people to split the bill?"))

calculation = (total_bill + (total_bill * (tip_amount/100)))/number_people

print(calculation)