#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("what was the total bill? $")
tip = input("What was the percentage tip you would like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
bill_as_float = float(bill)
tip_as_float = float(tip)
people_as_int = int(people)
tip_as_float = tip_as_float / 100
tip_as_float = tip_as_float + 1
total_bill_as_float = bill_as_float * tip_as_float
each_person_pay = total_bill_as_float / people_as_int
each_person_pay_rounded = round(each_person_pay, 2)
each_person_pay_rounded = "{:.2f}".format(each_person_pay)
print(f"Each Person Should Pay: ${each_person_pay_rounded}")