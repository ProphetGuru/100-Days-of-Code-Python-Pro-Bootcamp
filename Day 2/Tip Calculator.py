#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

restaurant_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people are to split the bill? "))
each_person_pays = round(restaurant_bill * (1+ (tip_percent/100))/number_of_people, 2)
print(f"Each person should pay: ${each_person_pays}")
