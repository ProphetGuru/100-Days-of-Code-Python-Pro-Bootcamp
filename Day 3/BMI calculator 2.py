print("")
print("May I present to you the computer BMI calculator:")
print("")
print("The calculator uses your height & weight to determine your BMI.")
# =============================================================================
# Exercise 2 - BMI 2.0 - Instructions
# Write a program that interprets the Body Mass Index (BMI) 
# based # on a user's weight and height.
# 
# It should tell them the interpretation of their BMI based on the BMI value.
# 
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# 
# 
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# 
# Warning you should round the result to the nearest whole number. 
# The interpretation message needs to include the words in bold 
# from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
# 
# Example Input
# weight = 85
# height = 1.75
# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325
# Your BMI is 28, you are slightly overweight.
# 
# 
# The testing code will check for print output that is formatted like 
# one of the lines below:
# 
# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."
# 
# Hint: 
# Try to use the exponent operator in your code.
# Remember to round your result to the nearest whole number.
# Make sure you include the words in bold from the interpretations.
# =============================================================================


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / (float(height) **2)


if BMI < 18.5:
    print("Your BMI is", int(round(BMI, 2)), "you are \033[1munderweight\033[0m.")

elif BMI < 25:
    print("Your BMI is", int(round(BMI, 2)), "you have a \033[1mnormal weight\033[0m.")

elif BMI < 30:
    print("Your BMI is", int(round(BMI, 2)), "you are \033[1mslightly overweight\033[0m.")

elif BMI < 35:
    print("Your BMI is", int(round(BMI, 2)), "you are \033[1mobese\033[0m.")

else: 
    print("Your BMI is", int(round(BMI, 2)), "you are \033[1mclinically obese\033[0m.")

