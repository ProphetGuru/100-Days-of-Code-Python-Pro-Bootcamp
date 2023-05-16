#************************** Rollercoaster ride part 2 ************************

# This program greets the user and asks for their height in centimeters
# This code prompts the user for their height and age, and then uses conditional 
# statements to determine whether they are eligible to ride the rollercoaster 
# and how much they should pay. If the user is over 120cm tall and over 18 years old, 
# they pay $12. If they are over 120cm tall but under 18 years old, they pay $7. 
# If they are less than 120cm tall, they are not eligible to ride.
# if they want a photo: Add $3
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

#                                    or 

# if condition 1: 
#    do A
# if condition 2: 
#    do B
# if condition 3: 
#    do C
# =============================================================================
    

# Greet the user
print("Welcome to the fabulous Rollercoaster!")

#Checks if the user's height is greater than 120cm
height = int(input("What is your height in cm, please? "))
bill = 0
# If user is taller than 120cm, the code asks for their age to calculate the ticket price
if height > 120:
    age = int(input("How old are you? "))

# If the user is 18 years old or older, they will be charged $12
    if age < 12:
        bill = 5 
        print("You can ride. You`re getting the 'Kiddie-Discount'. That`ll be $5. Enjoy it while it lasts")

# If the user is between 12 and 18 years old, they will be charged $7
    elif age <=18:
        bill = 7
        print("You can ride. That`ll be $7, please. Thank you and enjoy your ride")

# everyone else who is not younger than 12, and not between 12 and 18 pays full fare, $12.
    else:
        bill = 12
        print("You can ride. That`ll be $12, please. Thank you and enjoy your ride") 

#Ask the user if he/she wants a phone
    photo = input("Would you like a picture taken of you? ('y' or 'n')? ")
    if photo == "y":
        # Add $3 to their total bill
        bill += 3
    print(f"Awrighty... Your final bill is {bill}")

#If the user is shorter than 120cm, they will not be allowed to ride the rollercoaster
else: 
    print("Sorry mate, todays not your day. Wait until you`re at least 120cm tall")
    
