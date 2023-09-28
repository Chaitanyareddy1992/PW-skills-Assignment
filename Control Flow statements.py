#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a Python program to check if a given number is positive or negative.

# In[2]:


# Enter the number to check positive or negative number
n = float(input("Enter a number:"))
if n > 0:
    print("The number is positive")
elif n < 0:
    print("The number is negative")
else:
    print("The number is zero")


# ### 2. Create a program that determines if a person is eligible to vote based on their age.

# In[3]:


# Enter the age as input
age = int(input("Enter your age:"))
# check if person is eligible to vote
if age >= 18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")    


# ### 3. Develop a program to find the maximum of two numbers using if-else statements.

# In[6]:


# Enter the two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
# compare two numbers which is maximum
if num1 > num2:
    maximum = num1
else: 
        maximum = num2
        print("The maximum number is:",maximum)


# ### 4. Write a Python script to classify a given year as a leap year or not.

# In[9]:


# Given the input of a year
year = int(input("Enter a year:"))

if(year %4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# ## 5. Create a program that checks whether a character is a vowel or a consonant.

# In[15]:


# Get a character as input from user
char = input("Enter a character:")
# convert character to lower case to handle both upper and lower case
char = char.lower()
# check if character is vowel or consonant
if char.isalpha() and len(char) == 1:
    if char in "aeiou":
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")        


# ## 6. Implement a program to determine whether a given number is even or odd

# In[16]:


# check whether the given number is odd or even
def is_even_or_odd(number):
    if number % 2 == 0:
        return f'{number} is even'
    else:
        return f'{number} is odd'
   # try input from the user 
try:
    number = int(input("enter a number:"))
    result = is_even_or_odd(number)
    print(result)
except ValueError:
    print("Invalid input.Please Enter a valid input")


# ### 7. Write a Python function to calculate the absolute value of a number without using the abs() function

# In[24]:


def calculate_absolute_value(number):
    if number < 0:
        return -number
    else:
        return number

num = float(input("Enter a number:"))
absolute_value = calculate_absolute_value(num)
print(f"The absolute value of{num} is {absolute_value}")           


# ## 8. Develop a program that determines the largest of three given numbers using if-else statements

# In[25]:


def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return3
        
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    num3 = float(input("Enter the third number:"))
    
    largest = find_largest_number(num1, num2, num3)
    print(f"The largest number is:{largest}")
except valueError:
    print("Invalid input. Please enter the valid numbers.")


# ### 9. Create a program that checks if a given string is a palindrome

# In[30]:


def is_palindrome(input_string):
    removed_string = input_string.replace(" ","").lower()
    return removed_string == removed_string[::-1]
user_input = input("Enter a string:")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome")
else:
     print(f"{user_input} is not a palindrome")     


# ## 10. Write a Python program to calculate the grade based on a student's score

# In[32]:


def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 35 <= score < 60:
        return "E"
    elif 0 <= score < 35:
        return "F"
    else:
        return "Invalid score"
    
try:
    score = float(input("Enter the student score:"))
    
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The student grade is: {grade}")
    else:
        print("Score must be in between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid numeric score.")


# # Nested If-Else Statements:

# 11. Write a program to find the largest among three numbers using nested if-else statements.

# In[34]:


num1 = float(input("Enter the First number:"))
num2 = float(input("Enter the Second number:"))
num3 = float(input("Enter the Third number:"))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
        largest = num2
    else:
        largest = num3
        
print(f"The largest number among {num1},{num2} and {num3} is the {largest}")        


# ## 12. Implement a program to determine if a triangle is equilateral, isosceles, or scalene.

# In[1]:


# length of three sides of triangle
side1 = float(input("Enter the length of the first side:"))
side2 = float(input("Enter the length of the Second side:"))
side3 = float(input("Enter the length of the Third side:"))
# check type of triangle using else if-else elif statements
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "scalene"
    
print(f"The traingle with side lengths {side1},{side2} and {side3} is {triangle_type}")    


# ## 13. Develop a program that checks if a year is a leap year and also if it is a century year.

# In[4]:


year = int(input("Enter a year:"))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
is_century_year = (year % 100 == 0)

if is_leap_year and is_century_year:
    print(f"{year} is a leap year and a century year.")
elif is_leap_year:
    print(f"{year} is a leap year but not a century year.")
else:
    print(f"{year} is not a leap year.")


# ## 14. Write a Python script to determine if a number is positive, negative, or zero.

# In[5]:


# Enter the number 
number = float(input("Enter a number:"))
# check whether the given number is positive, negative or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# ## 15. Create a program to check if a person is a teenager (between 13 and 19 years old).

# In[6]:


# Enter the age
age = int(input("Enter your age:"))

if 13 <= age <= 19:
    print("You are a teenager")
else:
    print("you are not a teenager")


# ### 16. Develop a program that determines the type of angle based on its measure (acute, obtuse, or right).

# In[8]:


# Enter the angle measure input
angle_measure = float(input("Enter the angle measure in degrees:"))
# Determine the type of angle
if angle_measure < 90:
    angle_type = "acute"
elif angle_measure == 90:
    angle_type = "right"
else:
    angle_type = "obtuse"
    
print(f"The angle with a measure of {angle_measure} degrees is a {angle_type} angle.")    


# ## 17. Write a Python program to calculate the roots of a quadratic equation.

# In[9]:


# import math module to use for square root function
import math

a = float(input("Enter the coefficient 'a':"))
b = float(input("Enter the coefficient 'b':"))
c = float(input("Enter the coefficient 'c':"))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"roots are real and distinct:{root1} and {root2}")
elif discriminant == 0:
    
    root = -b/ (2*a)
    print(f"Root is real and equal:{root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) /(2*a)
    print(f"Roots are complex:{real_part} + {imaginary_part}i and {real_part}-{imaginary_part}i")


# ### 18. Implement a program to determine the day of the week based on a user-provided number (1 for Monday, 2 for Tuesday, etc.).

# In[11]:


# Enter the number for days of week
day_number = int(input("Enter a number(1 for Monday, 2 for Tuesday, etc.):"))
# Define a list of day names
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]
# check the provided number is in a valid range
if 1<= day_number <= 7:
# subtract 1 from input to access correct index in list    
    day_name = days_of_week[day_number-1]
    print(f"The day corresponding to {day_number} is {day_name}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")


# ## 19. Create a program that determines if a year is a leap year and also if it is evenly divisible by 400.

# In[17]:


# Enter the year
year = int(input("Enter a year:"))
# check year is even and divisible by 400
is_leap_year = (year % 4 == 0) and (year % 100 == 0 != 0 or year % 400 == 0)
is_divisible_by_400 = (year % 400 == 0)
# print results
if is_leap_year:
    print(f"{year} is a leap year.")
    if is_divisible_by_400:
        print(f"{year} is also evenly divisible by 400.")
else:
    print(f"{year} is not a leap year.")


# ### 20. Develop a program that checks if a given number is prime or not using nested if-else statements.

# In[1]:


# Enter the input number
number = int(input("Enter a number:"))
# check if number is greater than 1
if number > 1:
 # check factors
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
            print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# # Elif statements

# ## 21. Write a Python program to assign grades based on different ranges of scores using elif statements.

# In[2]:


score = float(input("Enter the score:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid input"
    
print(f"The grade for the score {score} is {grade}.")    


# ## 22. Implement a program to determine the type of a triangle based on its angles.

# In[9]:


# Enter the three angles of a triangle
angle1 = float(input("Enter the First angle in degrees:"))
angle2 = float(input("Enter the second angle in degrees:"))
angle3 = float(input("Enter the Third angle in degrees:"))
# check all angles to transform a valid triangle
if angle1 + angle2 + angle3 == 180:
    
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        triangle_type = "acute"
    elif angle1 == 90 and angle2 == 90 and angle3 == 90:
        triangle_type = "right"
    else:
        triangle_type = "obtuse"
    print(f"The triangle with angles are {angle1}, {angle2}, and {angle3} is a {triangle_type} triangle.")
else:
    print("Enter the correct angles to form a valid triangle.")


# ### 23. Develop a program to categorize a given person's BMI into underweight, normal, overweight, or obese using elif statements.

# In[2]:


weight = float(input("Enter weight in kilograms:"))
Height = float(input("Enter the Height in meters:"))

bmi = weight/(Height**2)

if bmi< 30:
    category = "underweight"
elif 30 <= bmi < 49.9:
    category = "Normal"
elif 50 <= bmi < 79.9:
    category = "overweight"
else:
    category = "obese"
print(f"The person's BMI is {bmi:.2f}, which is categorized as {category}.")    


# ### 24. Create a program that determines whether a given number is positive, negative, or zero using elifstatements.

# In[3]:


# Enter the number as input from user
number = float(input("Enter a number:"))
# check whether the number is positive, negative or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# ### 25. Write a Python script to determine the type of a character (uppercase, lowercase, or special) using elifstatements.

# In[7]:


# Enter the character as input from user
char = input("Enter a character:")
# check type of character using alphanumeric
if char.isalpha():
    if char.islower():
        print(f"The character '{char}' is lowercase.")
    elif char.isupper():
        print(f"The character '{char}' is uppercase.")
else:
    print(f"The character '{char}' is special (non-alphabetic).")


# ### 26. Implement a program to calculate the discounted price based on different purchase amounts using elif statements.

# In[10]:


purchase_amount = float(input("Enter the purchase amount:"))

discount_rate1 = 0.05
dicsount_rate2 = 0.10
discount_rate3 = 0.15

if purchase_amount >= 1000:
    discount_price = purchase_amount *(1-discount_rate3)
    discount_percent = 15
elif purchase_amount >= 500:
    discount_price = purchase_amount *(1-discount_rate2)
    discount_percent = 10
elif purchase_amount >= 100:
    discount_price = purchase_amount *(1-discount_rate1)
    discount_percent = 5
else:
    discount_price = purchase_amount
    discount_percent = 0

print(f"Original price: ${purchase_amount:.2f}")
print(f"Discount price is:${discount_price:.2f}")
print(f"Discount percentage is:${discount_percent:.2f}")


# ### 27. Develop a program to calculate the electricity bill based on different consumption slabs using elif statements.

# In[12]:


# Get the electricity consumption in kilowatt-hours (kWh) from the user
consumption = float(input("Enter the electricity consumption in kWh: "))

# Define electricity rate slabs and corresponding rates
slab1_limit = 100  # kWh
slab2_limit = 300  # kWh
slab3_limit = 500  # kWh
rate_slab1 = 0.15  # $/kWh for slab 1
rate_slab2 = 0.20  # $/kWh for slab 2
rate_slab3 = 0.25  # $/kWh for slab 3
base_charge = 20.0  # $ base charge

# Calculate the electricity bill using elif statements
if consumption <= slab1_limit:
    bill = base_charge + consumption * rate_slab1
elif consumption <= slab2_limit:
    bill = base_charge + (slab1_limit * rate_slab1) + ((consumption - slab1_limit) * rate_slab2)
elif consumption <= slab3_limit:
    bill = base_charge + (slab1_limit * rate_slab1) + ((slab2_limit - slab1_limit) * rate_slab2) + ((consumption - slab2_limit) * rate_slab3)
else:
    bill = base_charge + (slab1_limit * rate_slab1) + ((slab2_limit - slab1_limit) * rate_slab2) + ((slab3_limit - slab2_limit) * rate_slab3) + ((consumption - slab3_limit) * rate_slab3)

# Print the electricity bill
print(f"Electricity bill for {consumption} kWh: ${bill:.2f}")


# ### 28. Create a program to determine the type of quadrilateral based on its angles and sides using elif statements.

# In[13]:


angle1 = float(input("Enter the First angle in degrees:"))
angle2 = float(input("Enter the second angle in degrees:"))
angle3 = float(input("Enter the Third angle in degrees:"))
angle4 = float(input("Enter the Fourth angle in degrees:"))
side1 = float(input("Enter the length of side 1:"))
side2 = float(input("Enter the length of side2:"))
side3 = float(input("Enter the length of side3:"))
side4 = float(input("Enter the length of side4:"))

if angle1 == angle2 == angle3 == angle4 == 90:
    if side1 == side2 == side3 ==side4:
        quadrilateral_type = "square"
    else:
        quadrilateral_type = "rectangle"
elif angle1 == angle3 and angle2 == angle4 and angle1 + angle2 == 180:
    if side1 == side3 and side2 == side4:
        quadrilateral_type = "kite"
    else:
        quadrilateral_type = "parallelogram"
elif side1 == side2 == side3 == side4:
    if angle1 == angle2 == angle3 == angle4:
        quadrilateral_type = "rhombus"
    else:
        quadrilateral_type = "quadrilateral"
else:
    quadrilateral_type = "unknown"

# Print the type of quadrilateral
if quadrilateral_type != "unknown":
    print(f"The quadrilateral is a {quadrilateral_type}.")
else:
    print("The quadrilateral type is unknown based on the provided angles and sides.")        


# ### 29. Write a Python script to determine the season based on a user-provided month using elif statements.

# In[16]:


# Enter the month as input from the user
month = input("Enter a month (e.g., January, February, etc.): ")

# Convert the input to lowercase for case-insensitive comparison
month = month.lower()

# Check the season based on the month using elif statements
if month in ("January", "february", "March"):
    season = "winter"
elif month in ("april", "may", "june"):
    season = "summer"
elif month in ("june", "july", "august"):
    season = "spring"
elif month in ("september", "october", "november"):
    season = "autumn"
else:
    season = "unknown"

# Print the determined season
if season != "unknown":
    print(f"The season for {month.capitalize()} is {season}.")
else:
    print("Unknown month. Please enter a valid month name.")


# ### 30. Implement a program to determine the type of a year (leap or common) and month (30 or 31 days) using elif statements.

# In[18]:


# Enter the month and year as input
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

# check year is a leap year using ifelse statement
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    year_type = "leap"
else:
    year_type = "common"

# Check the number of days in the month using elif statements
if month == 2:
    if year_type == "leap":
        days_in_month = 29
    else:
        days_in_month = 28
elif month in (4, 6, 9, 11):
    days_in_month = 30
else:
    days_in_month = 31

# Print the type of year and the number of days in the month
print(f"The year {year} is a {year_type} year.")
print(f"The month {month} has {days_in_month} days.")


# # Basic level

# ## 1. Write a Python program that checks if a given number is positive, negative, or zero.

# In[19]:


# Enter the number as input
number = float(input("Enter a number:"))
# check whether given number is positive, negative or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
   


# ### 2. Create a program to determine if a person is eligible to vote based on their age.

# In[20]:


# Enter the age of input
age = int(input("Enter the age:"))
# check whether the person is eligible to vote or not
if age > 18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")


# ### 3. Write a program to find the maximum of two given numbers using conditional statements.

# In[22]:


# Enter the two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
# check whether the given number is maximum or not
if num1 > num2:
    maximum = num1
else:
    maximum = num2
print(f"The maximum number between {num1} and {num2} is {maximum}.")    


# ### 4. Develop a program that calculates the grade of a student based on their exam score.

# In[23]:


# Enter the input of exam scores
exam_score = float(input("Enter the exam score: "))

# Define grade boundaries
A_grade = 90
B_grade = 80
C_grade = 70
D_grade = 60

# calculate grades based upon exam scores
if exam_score >= A_grade:
    grade = "A"
elif exam_score >= B_grade:
    grade = "B"
elif exam_score >= C_grade:
    grade = "C"
elif exam_score >= D_grade:
    grade = "D"
else:
    grade = "F"

# Print the calculated grade
print(f"The student's grade for the exam score {exam_score} is {grade}.")


# ### 5. Create a program that checks if a year is a leap year or not.

# In[24]:


# Enter the year as input
year = int(input("Enter a year:"))
# check whether the year is leap year or not
if(year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# ### 6. Write a program to classify a triangle based on its sides' lengths.

# In[25]:


side1 = float(input("Enter the length of side1:"))
side2 = float(input("Enter the length of side2:"))
side3 = float(input("Enter the length of side3:"))

if side1 == side2 == side3:
    triangle_type = "equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type ="isosceles"
else:
    triangle_type = "scalene"
print(f"The traingle with side lengths {side1},{side2}, and{side3} is a {triangle_type} triangle.")    


# ### 7. Build a program that determines the largest of three given numbers.

# In[26]:


# Enter the number
num1 = float(input("Enter the First number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the Third number:"))
# check which number is largest among three numbers 
if num1 >= num2 and num2 >=num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number among {num1},{num2} and {num3} is {largest}.")    


# ### 8. Develop a program that checks whether a character is a vowel or a consonant.

# In[27]:


# Enter a character
character = input("Enter a character:")
# convert character to lowercase insensitive comparison
character = character.lower()
# check whether is a vowel or a consonant
if character.isalpha() and len(character) == 1:
    if character in "aeiou":
        print(f"The character '{character}' is a vowel.")
    else:
        print(f"The character '{character}'is a consonant.")
else:
    print("Please enter a single alphabetic character.")


# ### 9. Create a program to calculate the total cost of a shopping cart based on discounts.

# In[28]:


item_prices = {
    "item1":10.0,
    "item2":20.0,
    "item3":15.0,
}
item_quantities = {
    "item1":3,
    "item2":2,
    "item3":4,
}
total_cost = sum(item_prices[item]*item_quantities[item]for item in item_prices)

if total_cost >= 50:
    total_cost *=0.9
elif total_cost >= 30:
    total_cost *= 0.95
    
print(f"The Total cost of shopping cart is:${total_cost:.2f}")    


# ### 10. Write a program that checks if a given number is even or odd.

# In[31]:


# Enter the number
number = int(input("Enter a number:"))
# check whether the number is even or odd
if number %2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# # Intermediate level

# ### 11. Write a program that calculates the roots of a quadratic equation

# In[1]:


import math

a = float(input("Enter the coefficient a:"))
b = float(input("Enter the coefficient b:"))
c = float(input("Enter the coefficient c:"))

discriminant = b**2-4*a*c

if discriminant > 0:
    root1 = (-b +math.sqrt(discriminant)) / (2*a)
    root2 = (-b -math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and distinct:{root1} and {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"The root is real and repeated: {root1}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
    


# ### 12. Create a program that determines the day of the week based on the day number (1-7).

# In[3]:


day_number = int(input("Enter a day number (1-7):"))

days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if 1 <= day_number <= 7:
    
    day_name = days_of_week[day_number - 1]
    print(f"The day corresponding to day number {day_number} is {day_name}.")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")    


# ### 13. Develop a program that calculates the factorial of a given number using recursion.

# In[9]:


# Define a recursive function to calculate the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from the user
num = int(input("Enter a non-negative integer: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")


# ### 14. Write a program to find the largest among three numbers without using the `max()` function.

# In[11]:


# Enter the Three numbers
num1 = float(input("Enter the First number"))
num2 = float(input("Enter the Second number"))
num3 = float(input("Enter the Third number"))
# create a list of three numbers
numbers = [num1, num2, num3]
# sort list in descending order
numbers.sort(reverse = True)
# largest number will now be first index of sorted list
largest = numbers[0]
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")


# ### 15. Create a program that simulates a basic ATM transaction menu.

# In[14]:


balance = 5000.0

def check_balance():
    print(f"Your account balance is ${balance:.2f}")
    
def deposit():
    global balance
    amount = float(input("Enter the amount to be deposit:"))
    if amount > 0:
        balance += amount
        print(f"${amount:2f} has been deposited successfully.")
    else:
        print("Invalid amount. Please enter a positive value.")
        
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw:"))
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount:.2f} has been withdraw successfully.")
    else:
        print("Insufficient funds or invalid amount.")
        
# ATM transaction loop
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the ATM. Have a nice day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


# ### 16. Build a program that checks if a given string is a palindrome or not.

# In[16]:


# Check whether if string is palindrome
def is_palindrome(input_str):
    # remove spaces and convert it to lowercase
    cleaned_str = ''.join(input_str.split()).lower()
    # check if cleaned string is equal to reverse
    return cleaned_str == cleaned_str[::-1]

# Get a string as input from the user
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")


# ### 17. Write a program that calculates the average of a list of numbers, excluding the smallest and largest values.

# In[21]:


def calculate_avg_excluding_extremes(numbers):
    if len(numbers) < 3:
        return None
    sorted_numbers = sorted(numbers)
    trimmed_numbers = sorted_numbers[1:-1]
    
    average = sum(trimmed_numbers)/len(trimmed_numbers)
    return average

input_numbers = input("Enter a list of numbers seperated by spaces: ").split()
numbers = [float(num) for num in input_numbers]

average = calculate_avg_excluding_extremes(numbers)

if average is not None:
    print(f"The average (excluding extremes)is:{average:.2f}")
else:
    print("Not enough elements to calculate the average (need at least 3 numbers).")


# ### 18. Develop a program that converts a given temperature from Celsius to Fahrenheit.

# In[23]:


# convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Get temperature in celsius as input
celsius = float(input("Enter the Temperature in celsius:"))
# convert celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees fahrenheit.")


# ### 19. Create a program that simulates a basic calculator for addition, subtraction, multiplication, and division.

# In[25]:


def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multiply(x, y):
    return x * y
def devide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
while True:
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    
    choice = input("Enter your choice(1/2/3/4/5):")
    
    if choice == "5":
        print("Exit!")
        break
    
    if choice not in ["1","2","3","4"]:
        print("Invalid choice. Please select a valid option.")
        continue
        
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))
    
    if choice == "1":
        result = add(num1, num2)
        operation = "addition"
    elif choice == "2":
        result = sub(num1, num2)
        operation = "subtraction"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == "4":
        result = divide(num1, num2)
        operation = "division"
    print(f"The result of {operation} is: {result}")     


# ### 20. Write a program that determines the roots of a cubic equation using the Cardano formula.

# In[27]:


import math

# Function to find the roots of a cubic equation using Cardano's formula
def cubic_roots(a, b, c, d):
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    discriminant = (q/2)**2 + (p/3)**3

    if discriminant > 0:
        u = (-q/2 + discriminant**0.5)**(1/3)
        v = (-q/2 - discriminant**0.5)**(1/3)
        real_root = u + v
        imaginary_part = (3**0.5) * (u - v) / 2
        root1 = real_root - b / (3*a)
        root2 = -((real_root + 1j * imaginary_part) / 2) - b / (3*a)
        root3 = -((real_root - 1j * imaginary_part) / 2) - b / (3*a)
    elif discriminant == 0:
        if q < 0:
            root1 = (3*q)**(1/3) / (3*a) - b / (3*a)
            root2 = -(2 * (3*q)**(1/3)) / (3*a) - b / (3*a)
            root3 = root2
        else:
            root1 = -2 * (q)**(1/3) / (3*a) - b / (3*a)
            root2 = root1
            root3 = (q)**(1/3) / (3*a) - b / (3*a)
    else:
        theta = math.acos(-q/2 * (discriminant**(-3/2)))
        root1 = 2 * math.sqrt(-p/3) * math.cos(theta/3) - b / (3*a)
        root2 = 2 * math.sqrt(-p/3) * math.cos((theta + 2*math.pi)/3) - b / (3*a)
        root3 = 2 * math.sqrt(-p/3) * math.cos((theta + 4*math.pi)/3) - b / (3*a)

    return root1, root2, root3

# Get coefficients as input from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))

# Calculate the roots
roots = cubic_roots(a, b, c, d)

# Print the roots
print(f"The roots of the cubic equation are: {roots}")


# # Advanced Level:

# ### 21. Create a program that calculates the income tax based on the user's income and tax brackets.

# In[28]:


# Enter the tax brackets
tax_brackets = [(0, 9700, 0.10),
                (9701, 39475, 0.12),
                (39476, 84200, 0.22),
                (84201, 160725, 0.24),
                (160726, 204100, 0.32),
                (204101, 510300, 0.35),
                (510301, float("inf"), 0.37)]

# Function to calculate income tax
def calculate_income_tax(income):
    tax_owed = 0
    remaining_income = income

    for bracket in tax_brackets:
        min_income, max_income, rate = bracket
        if remaining_income <= 0:
            break
        taxable_income = min(max_income - min_income, remaining_income)
        tax_owed += taxable_income * rate
        remaining_income -= taxable_income

    return tax_owed

# Get the user's income as input
income = float(input("Enter your annual income: "))

# Calculate income tax
income_tax = calculate_income_tax(income)

# Print the income tax amount
print(f"Your income tax is: ${income_tax:.2f}")


# ### 22. Write a program that simulates a rock-paper-scissors game against the computer.

# In[29]:


import random

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break


# ### 23. Develop a program that generates a random password based on user preferences (length, complexity).

# In[30]:


import random
import string

# Function to generate a random password
def generate_password(length, include_uppercase, include_digits, include_special_chars):
    # Define character sets based on complexity preferences
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets based on preferences
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "Please select at least one character set for complexity."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get user preferences
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_digits = input("Include digits? (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

# Generate the password
password = generate_password(length, include_uppercase, include_digits, include_special_chars)

# Print the generated password
print(f"Generated Password: {password}")


# ### 24. Create a program that implements a simple text-based adventure game with branching scenarios.

# In[1]:


import random

def start_game():
    print("welsome to the Text Adventure game!")
    print("You find yourself in a dark forest. You can go left or right.")
    choice = input("which way do you want to go? (left/right):").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        start_game()
        
def left_path():
    print("\n you choose to go left.")
    print("You come across a river with a bridge. Do you want to cross it or go back?")
    choice = input("cross the bridge or go back? (cross/back):").lower()
    
    if choice == "cross":
        cross_bridge()
    elif choice == "back":
        start_game()
    else:
        print("Invalid choice.Please enter 'cross'or 'back'.")
        left_path()
        
def right_path():
    print("\n you choose to go right.")
    print("you encounter a cave entrance. Do you want to enter the cave or return?")
    choice = input("Enter the cave or return? (enter/return):").lower()
    
    if choice == "enter":
        enter_cave()
    elif choice == "return":
        start_game()
    else:
        print("Invalid choice.Please enter 'enter' or 'return'.")
        right_path()
        
def cross_bridge():
    print("\n you cross the bridge and continue your journey.")
    print("Ahead, you see a treasure chest! What do you do?")
    choice = input("Open the chest or ignore it? (open/ignore): ").lower()
    
    if choice == "open":
        print("\nCongratulations! You found a treasure chest full of gold. You win!")
    elif choice == "ignore":
        print("\nYou decide to ignore the chest and continue your adventure.")
        continue_adventure()
    else:
        print("Invalid choice. Please enter 'open' or 'ignore'.")
        cross_bridge()


def enter_cave():
    print("\nYou enter the dark cave.")
    print("Inside the cave, you find a sleeping dragon. What do you do?")
    choice = input("Attempt to sneak past or try to wake the dragon? (sneak/wake): ").lower()
    
    if choice == "sneak":
        print("\nYou manage to sneak past the dragon and exit the cave safely.")
        continue_adventure()
    elif choice == "wake":
        print("\nThe dragon wakes up and breathes fire, turning you into ashes. Game over!")
    else:
        print("Invalid choice. Please enter 'sneak' or 'wake'.")
        enter_cave()

# Continue the adventure
def continue_adventure():
    print("\nYou continue your adventure.")
    print("You can go deeper into the forest, or you can choose to end your journey.")
    choice = input("Go deeper into the forest or end your journey? (forest/end): ").lower()
    
    if choice == "forest":
        start_game()
    elif choice == "end":
        print("\nThanks for playing the Text Adventure Game!")
        exit()
    else:
        print("Invalid choice. Please enter 'forest' or 'end'.")
        continue_adventure()

# Start the game
start_game()        


# ### 25. Build a program that solves a linear equation for x, considering different cases.

# In[3]:


def solve_linear_equation():
    print("Linear equation solver: ax+b = 0")
    
    try:
        a = float(input("Enter the coefficient 'a':"))
        b = float(input("Enter the coefficient 'b':"))
    except valueError:
        print("Invalid input. Please enter valid numerical coefficients.")
        return
    
    if a == 0:
        if b == 0:
            print("Infinite solutions: 0x = 0")
        else:
            print("No Solution: 0x + {} = 0".format(b))
    else:
        x = -b/a
        print("Solution: x={}".format(x))
solve_linear_equation()        


# ### 26. Write a program that simulates a basic quiz game with multiple-choice questions and scoring.  

# In[4]:


class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        
    def display_question(self):
        print(self.question)
        for index, option in enumerate(self.options, start=1):
            print(f"{index}.{option}")
    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

def run_quiz(questions):
    score = 0
    for question in questions:
        question.display_question()
        try:
            user_answer = int(input("Enter the number of your answer:"))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue
        if 1 <= user_answer <= len(question.options):
            if question.is_correct(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. The correct answer was {question.correct_answer}:{question.options[question.correct_answer -1]}\n")
        else:
            print("Invalid answer number. Please choose a valid option.\n")
    print(f"Quiz completed! your score is:{score}/{len(questions)}")
    
question1 = QuizQuestion("What is the capital of India?",["NewDelhi","Bombay","Hyderabad","Goa"], 1)
question2 = QuizQuestion("Which planet is known as the red planet?",["Earth","Mars","Jupyter","Venus"], 2)
question3 = QuizQuestion("What is the largest mammal in the world?",["Elephant","Giraffe","Blue whale","Leopard"], 3)

quiz_questions = [question1, question2, question3]

run_quiz(quiz_questions)


# ### 27. Develop a program that determines whether a given year is a prime number or not.

# In[5]:


def is_prime(year):
    if year <= 1:
        return False
    if year <= 3:
        return True
    
    for i in range(2, int(year**0.5)+1):
        if year % i == 0:
            return False
    return True

try:
    year = int(input("Enter a year to check if its prime:"))
except valueError:
    print("Invalid input. please enter a valid year.")
else:
    if is_prime(year):
        print(f"{year} is a prime year.")
    else:
        print(f"{year} is not a prime year.")


# ### 28. Create a program that sorts three numbers in ascending order using conditional statements.

# In[6]:


# Enter the three numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
    exit()

# Using conditional statements to sort the numbers in ascending order
if num1 <= num2 <= num3:
    sorted_nums = (num1, num2, num3)
elif num1 <= num3 <= num2:
    sorted_nums = (num1, num3, num2)
elif num2 <= num1 <= num3:
    sorted_nums = (num2, num1, num3)
elif num2 <= num3 <= num1:
    sorted_nums = (num2, num3, num1)
elif num3 <= num1 <= num2:
    sorted_nums = (num3, num1, num2)
else:
    sorted_nums = (num3, num2, num1)

# Display the sorted numbers
print("Sorted numbers in ascending order:", sorted_nums)


# ### 29. Build a program that determines the roots of a quartic equation using numerical methods.

# In[12]:


import math
# function for finding roots
def equationroots(a,b,c):
    # calculate discriminant using formula
    dis = b*b - 4*a*c
    sqrt_val = math.sqrt(abs(dis))
  # calculate discriminant using formula  
    if dis > 0:
        print("real and different roots")
        print((-b + sqrt_val)/(2*a))
        print((-b - sqrt_val)/(2*a))
    # check condition for discriminant    
    elif dis == 0:
        print("real and different roots")
        print(-b/(2*a))
        # when discriminant is less than 0
    else:
        print("omplex roots")
        print(-b/(2*a),+i, sqrt_val)
        print(-b/(2*a),-i, sqrt_val)
        
a = 5
b = 10
c= -25

if a == 0:
    print("Input correct quadratic equation")
    
else:
    equationroots(a, b, c)


# ### 30. Write a program that calculates the BMI (Body Mass Index) and provides health recommendations based on the user's input.

# In[16]:


def bodymassindex(height, weight):
    return round((weight/ height**2),2)
h = float(input("Enter the height in meters "))
w = float(input("Enter the weight in kilograms "))

print("welcome to the BMi calculator")

bmi = bodymassindex(h,w)
print("your bmi is",bmi)

if bmi <= 18.5:
    print("you are under weight")
elif 18.5< bmi <= 24.9:
    print("You are normal")
elif 24.9 < bmi <= 29.9:
    print("you are overweight")
else:
    print("Enter the valid input")
    


# # Challenge Level:

# ### 31. Create a program that validates a password based on complexity rules (length, characters, etc.).

# In[31]:


import re

def is_valid_password(password):
   # check the password meets the character length of atleast 10 characters 
    if len(password) < 10:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!\@\#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|]', password):
        return False
    return True
password = input("Enter a password: ")

if is_valid_password(password):
    print("password is valid")
else:
    print("password is not valid . Please enter the correct password")
        


# ### 32. Develop a program that performs matrix addition and subtraction based on user input.

# In[1]:


# Enter the Matrix inputs
m1 = [list(map(int, input("Enter row:").split(" ")))
     for i in range(int(input("Enter Number of rows:")))]
m2 = [list(map(int, input("Enter row:").split(" ")))
     for i in range(int(input("Enter number of rows:")))]
# Addition of two matrices
print("Add Matrix:")
r = [[m1[i][j]+m2[i][j]
      for j in range(len(m1[0]))] for i in range(len(m1))]
print(r)
# subtraction of two matrices
print("Sub Matrix:")
r = [[m1[i][j]-m2[i][j]
     for j in range(len(m1[0]))] for i in range(len(m1))]
print(r)    


# ### 33. Write a program that calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

# In[6]:


def euclidean_gcd(a, b):
    while b:
        a, b = b, a%b
    return a

try:
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    
except valueError:
    print("Invalid input.Please enter a numerical value")
    exit() 
    
gcd = euclidean_gcd(num1, num2)
print(f"The gcd numbers of {num1} and {num2} is:",gcd)


# ### 34. Build a program that performs matrix multiplication using nested loops and conditional statements.

# In[2]:


# encoding the two matrices
A = [[1,2,3],[5,3,1],[7,9,8]]
B = [[3,4],[12,4],[8,14]]
 
# retrieving the sizes/dimensions of the matrices
p = len(A)
q = len(A[0])
 
t = len(B)
r = len(B[0])
 
if(q!=t):
   print("Error! Matrix sizes are not compatible")
   quit()
 
# creating the product matrix of dimensions p×r
# and filling the matrix with 0 entries
C = []
for row in range(p):
   curr_row = []
   for col in range(r):
       curr_row.append(0)
   C.append(curr_row)
 
 
# performing the matrix multiplication
for i in range(p):
   for j in range(r):
       curr_val = 0
       for k in range(q):
           curr_val += A[i][k]*B[k][j]
       C[i][j] = curr_val
 
print(C)


# ## 35. Create a program that simulates a basic text-based tic-tac-toe game against the computer.

# In[ ]:


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")

def get_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if player == "X":
            print("\nYour turn (X):")
            row, col = get_player_move(board)
        else:
            print("\nComputer's turn (O):")
            row, col = get_computer_move(board)

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"{player} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        player, computer = computer, player

if __name__ == "__main__":
    play_game()


# ### 36. Write a program that generates Fibonacci numbers up to a specified term using iterative methods.

# In[2]:


def gen_fibonacci(n):
    fibonacci_sequence = []
    
    if n <= 0:
        return fibonacci_sequence
    elif n ==1:
        return [0]
    elif n == 2:
        return [0,1]
    a, b = 0, 1
    fibonacci_sequence.append(a)
    fibonacci_sequence.append(b)
    
    for _ in range(2, n):
        a, b = b, a+b
        fibonacci_sequence.append(b)
    return fibonacci_sequence  

try:
    n = int(input("Enter the number of Fibonacci terms to generate: "))
    if n < 0:
        print("Please enter a non-negative integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Generate and display the Fibonacci sequence
fibonacci_sequence = gen_fibonacci(n)
print("Fibonacci Sequence:")
print(fibonacci_sequence)


# ### 37. Develop a program that calculates the nth term of the Fibonacci sequence using memoization.

# In[4]:


fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        
        result = fibonacci(n-1)+ fibonacci(n - 2)
    fib_cache[n] = result
    return result

try:
    n = int(input("Enter the value of n to find the nth Fibonacci term:"))
    if n < 0:
        print("Please enter a non-negative integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Calculate and display the nth Fibonacci term
result = fibonacci(n)
print(f"The {n}th Fibonacci term is: {result}")


# ### 38. Create a program that generates a calendar for a given month and year using conditional statements.

# In[7]:


import calendar

try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
    exit()
    
if month <1 or month >12:
    print("Invalid input. Please enter valid numerical values.")
    exit()
    
cal = calendar.month(year, month)
print("\ncalendar:")
print(cal)


# ### 39. Build a program that simulates a basic text-based blackjack game against the computer.

# In[ ]:


import random

# Initialize deck and player/computer hands
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

def deal_card():
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        rank = card['rank']
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            value += 11
            num_aces += 1
        else:
            value += int(rank)
    
    # Handle aces
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

def print_hand(hand):
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

# Game loop
while True:
    # Initialize a new round
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    print("\nWelcome to Blackjack!")
    print("Your hand:")
    print_hand(player_hand)
    
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Your current hand value: {player_value}")
        
        if player_value == 21:
            print("Blackjack! You win!")
            break
        elif player_value > 21:
            print("Bust! You lose!")
            break
        
        choice = input("Do you want to hit (h) or stand (s)? ").lower()
        if choice == 'h':
            player_hand.append(deal_card())
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please enter 'h' or 's'.")
    
    # Computer's turn
    while calculate_hand_value(computer_hand) < 17:
        computer_hand.append(deal_card())
    
    print("\nComputer's hand:")
    print_hand(computer_hand)
    
    player_value = calculate_hand_value(player_hand)
    computer_value = calculate_hand_value(computer_hand)
    
    if computer_value > 21:
        print("Computer busts! You win!")
    elif player_value > 21 or player_value < computer_value:
        print("Computer wins!")
    elif player_value > computer_value:
        print("You win!")
    else:
        print("It's a tie!")
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing Blackjack!")


# ### 40. Write a program that generates the prime factors of a given number using trial division.

# In[4]:


def get_prime_factors(n):
    prime_factors = []
    div = 2
    
    while div <= n:
        if n % div == 0:
            prime_factors.append(div)
            n = n // div
        else:
            div += 1
            
    return prime_factors

try:
    num = int(input("Enter a number to find its prime factors: "))
    if num <= 1:
        print("Please enter a positive integer greater than 1.")
    else:
        factors = get_prime_factors(num)
        if len(factors) == 0:
            print(f"{num} is a prime number.")
        else:
            print(f"The prime factors of {num} are: {', '.join(map(str, factors))}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

