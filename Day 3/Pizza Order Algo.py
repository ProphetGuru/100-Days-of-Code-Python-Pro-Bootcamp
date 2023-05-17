
# =============================================================================

# Exercise 4 - Pizza Order Practice
# Overview
# My Submissions/Test Runs
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# 
# Based on a user's order, work out their final bill.
# 
# Small Pizza: $15
# 
# Medium Pizza: $20
# 
# Large Pizza: $25
# 
# Pepperoni for Small Pizza: +$2
# 
# Pepperoni for Medium or Large Pizza: +$3
# 
# Extra cheese for any size pizza: + $1
# 
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
# e.g. When you hit run, this is what should happen:
# 
# 
# 
# Hint
# Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
# 🚨 Don't change the code below 👇

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇

# =============================================================================

# Greet the user
print("Welcome to Ibi Pizza shop!")
bill = 0

#Checks pizza
size = input("What size of Pizza do you want? 'S', 'M' or 'L'? ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

#Ask for pepper 
Pepe = input("Do you want peperoni? ('Y' or 'N')? ")
if Pepe == "Y":
# Add $3 to their total bill
    if size == "M" or size == "L":
        bill += 3
    
    else:
        bill +=2

Cheese = input("Do you want Cheese? ('Y' or 'N')? ")

if Cheese == "Y":
        bill += 1
    
print(f"Awrighty... Your final bill is {bill}")
