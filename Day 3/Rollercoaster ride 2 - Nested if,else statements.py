#************************** Rollercoaster ride part 2 ************************

# This program greets the user and asks for their height in centimeters
# This code prompts the user for their height and age, and then uses conditional 
# statements to determine whether they are eligible to ride the rollercoaster 
# and how much they should pay. If the user is over 120cm tall and over 18 years old, 
# they pay $12. If they are over 120cm tall but under 18 years old, they pay $7. 
# If they are less than 120cm tall, they are not eligible to ride.
# =============================================================================
# here is a quick recap of Nested conditional statements
# if condition1: 
#     if another condition:
#         do this
#     else: 
#         do this
# else: 
#     do this

#                                    or

# if condition 1:
#     do A
# elif condition 2: 
#     do B
# else: 
#     do this
# =============================================================================
    

# Greet the user
print("Welcome to the fabulous Rollercoaster!")

#Checks if the user's height is greater than 120cm
height = int(input("What is your height in cm, please? "))

# If user is taller than 120cm, the code asks for their age to calculate the ticket price
if height > 120:
    age = int(input("How old are you? "))

# If the user is 18 years old or older, they will be charged $12
    if age < 12:
        print("Oh you`re getting the 'Kiddie-Discount'. That`ll be $5. Enjoy it while it lasts")

# If the user is between 12 and 18 years old, they will be charged $7
    elif age <=18:
        print("That`ll be $7, please. Thank you and enjoy your ride")

# everyone else who is not younger than 12, and not between 12 and 18 pays full fare, $12.
    else:
        print("That`ll be $12, please. Thank you and enjoy your ride") 

#If the user is shorter than 120cm, they will not be allowed to ride the rollercoaster
else: 
    print("Sorry mate, todays not your day. Wait until you`re at least 120 tall")
    
    