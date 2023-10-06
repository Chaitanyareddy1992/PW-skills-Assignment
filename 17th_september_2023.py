#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a Python program to print numbers from 1 to 10 using a for loop

# In[3]:


for i in range(1,11):
    print(i)


# ## 2.Explain the difference between a for loop and a while loop in Python.

# In[9]:


items = ['Laptop','Mouse','Keyboard','Pen']
for item in items:
    print(item)


# In[11]:


items = ['Laptop','Mouse','Keyboard','Pen']
# Declare the index value
index = 0
# Enter the length of the items
items_len = len(items)
# Check the condition whether items length is greater than index or not
while index < items_len:
    # print the result for items index
    print(items[index])
    index = index+1


# ### 3.Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop

# In[12]:


total_sum = 0
# Enter the number of range from 1 to 100.
for number in range(1,101):
    # calculate the total sum of all numbers
    total_sum += number
    print("The total sum of number from 1 to 100 is:",total_sum)


# ### 4.How do you iterate through a list using a for loop in Python?

# In[14]:


my_list = [1,2,3,4,5]
for item in my_list:
    print(item)


# ### 5.Write a Python program to find the product of all elements in a list using a for loop

# In[16]:


# Enter the list of elements
my_list = [1,2,3,4,5]
# Initilalize variable to store product
product = 1
# using for loop to generate each element in a list
for num in my_list:
    product *= num
print("The product of all elements in the list is:", product)


# ### 6.Create a Python program that prints all even numbers from 1 to 20 using a for loop.

# In[18]:


# Enter the range of elements from 1 to 20
for number in range(1, 21):
    # check the number whether it is even or not
    if number %2 == 0:
        print(number)


# ### 7.Write a Python program that calculates the factorial of a number using a for loop 

# In[21]:


num = int(input("Enter a number"))

factorial = 1

if num < 0:
    print("Factorial is not applicable for negative numbers:")
elif num == 0:
    print("The Factorial of 0 is 1.")
else:
    for i in range(1, num+1):
        factorial *= i
print(f"The factorial of {num} in {factorial}.")        


# ### 8.How can you iterate through the characters of a string using a for loop in Python

# In[26]:


my_String = "Data Science"

for char in my_String:
    print(char)


# ### 9.Write a Python program to find the largest number in a list using a for loop

# In[29]:


# Enter the list of elements
new_list = [1,3,5,2,4,8,10,12,16,13]
# calculate maximum number of elements
max_num = new_list[0]
# use for loop to iterate through each number in list
for number in new_list:
    if number > max_num:
        max_num = number

print("The number in the list is:",max_num)        


# ### 10.Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop

# In[30]:


def print_fibonacci(limit):
   # Initialize first two fibonacci numbers 
    fib1, fib2 = 0, 1
    # print first two numbers
    print(fib1, fib2, end=" ")
    # use for loop to generate fibonacci numbers upto limit
    while fib1 + fib2 <= limit:
        fib3 = fib1 + fib2
        print(fib3, end=" ")
        fib1, fib2 = fib2, fib3
   # get limit from user     
limit = int(input("Enter the limit for Fibonacci sequence:"))

print_fibonacci(limit)


# ### 11.Write a Python program to count the number of vowels in a given string using a for loop

# In[31]:


def count_vowels(input_string):
    
    vowels = set("AEIOUaeiou")
    
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
input_string = input("Enter a string:")

vowel_count = count_vowels(input_string)
print("Number of vowels in the string is:",vowel_count)


# ### 12.Create a Python program that generates a multiplication table for a given number using a for loop

# In[35]:


num = int(input("Enter a number:"))
# range for multiplication from 1 to 10
start = 1
end = 10
# use for loop to generate multiplication table
print(f"Multiplication table for {num}:")
for i in range(start, end + 1):
    result = num * i
    print(f"{num}*{i}={result}")    


# ### 13.Write a Python program to reverse a list using a for loop

# In[36]:


new_list = [1,2,3,4,5]
reversed_list = []
# use for loop to generate reversed string
for item in reversed(new_list):
    reversed_list.append(item)
print("Original list:", new_list)
print("Reversed list:", reversed_list)


# ### 14.Write a Python program to find the common elements between two lists using a for loop

# In[37]:


# Enter the list of elements
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
common_elements = []
# use for loop to check list1 and list2 are common elements
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common_elements.append(item1)
print("Common elements in list1 and list2 is:",common_elements)                        


# ### 15.Explain how to use a for loop to iterate through the keys and values of a dictionary in Python

# In[40]:


new_dict = {'a':1, 'b':2, 'c':3}

for key, value in new_dict.items():
    print(f'key:{key}, value:{value}')


# ### 16.Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a for loop

# In[41]:


def gcd(a,b):
    while b:
        a, b = b, a%b
        return a
    # Enter the number of inputs from user
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

result = gcd(num1,num2)

print(f"The gcd of {num1} and {num2} is:", result)


# ### 17.Create a Python program that checks if a string is a palindrome using a for loop.

# In[42]:


def is_palindrome(input_string):
    cleaned_string = input_string.replace(" "," ").lower()
    
    start = 0
    end = len(cleaned_string) - 1
    
    for i in range(len(cleaned_string) // 2):
        if cleaned_string[start] != cleaned_string[end]:
            return False
        start += 1
        end -= 1
    return True
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome. ")


# ###  18.Write a Python program to remove duplicates from a list using a for loop

# In[43]:


new_list = [1,2,2,3,44,5,6,8,9,8]
# Initialize empty set to store unique elements
unique_list = []
# use for loop to iterate through original list
for item in new_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list with duplicates:",new_list)
print("List with out duplication:",unique_list)


# ### 19.Create a Python program that counts the number of words in a sentence using a for loop

# In[48]:


# Enter a sentence input
sentence = input("Enter a sentence:")
# Initialize a variable to word a count
word_count = 0
# using for loop to check the sentence for word_count
for char in sentence:
    if char == ' ' or char == '\t':
        word_count += 1
word_count += 1
print(f"The number of words in the sentence is:", {word_count})


# ### 20.Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop

# In[52]:


for number in range(1, 51):
    if number%2 != 0:
        print(number)


# ### 21.Write a Python program that checks if a given year is a leap year using a for loop

# In[53]:


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
   # Get the year from user 
year = int(input("Enter a year: "))
# check if year is leap year and print result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# ### 22.Create a Python program that calculates the square root of a number using a for loop

# In[56]:


def approximate_sqrt(number, iterations=10):
    guess = number / 2
    for _ in range(iterations):
        guess = (guess + number / guess) / 2
    return guess

number = float(input("Enter a number: "))

iterations = int(input("Enter the number of iterations (default is 10):") or "10")

result = approximate_sqrt(number, iterations)
print(f"The approximate square root of {number} is {result:.5f}")


# ### 23.Write a Python program to find the LCM (Least Common Multiple) of two numbers using a for loop

# In[57]:


def gcd(a, b):
    while b:
        a, b = b, a%b
        return a
    
def lcm(a,b):
    return (a * b)// gcd(a, b)

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

result = lcm(num1, num2)
print(f"The lcm of {num1} and {num2} is:",result)


# # if-else

# ### 1.Write a Python program to check if a number is positive, negative, or zero using an if-else statement

# In[21]:


try:
    # Enter the number from user
    num = float(input("Enter a number: "))

    # check if a number is positive , negative or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except Exception as e:
    print(e)


# ### 2.Create a Python program that checks if a given number is even or odd using an if-else statement

# In[18]:


try:
    num = int(input("Enter a number:"))
    if num%2 == 0:
        print("This is a Even number")
    else:
        print("This is a Odd number")
except Exception as e:
    print(e)


# ### 3.How can you use nested if-else statements in Python, and provide an example?

# In[29]:


try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("you are eligible to vote.")
        
        registered = input("Are you registered to vote? (yes/no): ").lower()
        
        if registered == "yes":
            print("Great make sure to cast your vote in the upcoming election.")
        elif registered == "no":
            print("Please consider registering to vote so you can participate in the election.")
        else:
            print("Invalid input. Please enter 'yes' or 'no' for voter registration status.")
    else:
        print("sorry, you are not eligible to vote. you must be atleast 18 years.")
except Exception as e:
    print(e)


# ### 4.Write a Python program to determine the largest of three numbers using if-else

# In[34]:


try:
    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    if num1 >= num2 and num2 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    print("The largest number among", num1, ",", num2, ", and", num3, "is", largest) 
except Exception as e:
    print(e)


# ### 5.Write a Python program that calculates the absolute value of a number using if-else

# In[28]:


try:
    num = float(input("Enter a number:"))
    if num < 0:
        absolute_value = -num
    else:
        absolute_value = num
    print("The absolute value of", {num}, "is", absolute_value) 
except exception as e:
    print(e)


# ### 6.Create a Python program that checks if a given character is a vowel or consonant using if-else

# In[38]:


try:
    char = input("Enter a character: ").lower() 
    
    if len(char) == 1 and char.isalpha():
        # check if a character is a vowel or consonant
        if char in 'aeiou':
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetic character.")
except Exception as e:
    print(f"An error occurred: {e}")


# ### 7.Write a Python program to determine if a user is eligible to vote based on their age using if-else

# In[39]:


try:
    # Enter the input of age
    age = int(input("Enter your age: "))
    # check if age is a positive integer
    if age <= 0:
        print("Invalid input. Age must be a Positive Integer.")
    else:
        # check if person age is eligible to vote or not
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("Sorry, you are not eligible to vote.")
except ValueError:
    print("Invalid Input. Please enter a valid positive number.")


# ### 8.Create a Python program that calculates the discount amount based on the purchase amount using if-else

# In[41]:


try:
    
    purchase_amount = float(input("Enter the Purchase amount:"))
    
    if purchase_amount < 0:
        print("Invalid input. Purchase amount cannot be negative.")
    else:
        if purchase_amount < 100:
            discount = 0
        elif purchase_amount < 500:
            discount = 0.05 * purchase_amount
        elif purchase_amount < 1000:
            discount = 0.1 * purchase_amount 
        else:
            discount = 0.15 * purchase_amount
        print(f"Discount_amount:${discount:.2f}")
except ValueError:
    print("invalid input. Please enter a valid numeric purchase amount.")
except Exception as e:
    print("An error occured:{e}")


# ### 9.Write a Python program to check if a number is within a specified range using if-else

# In[43]:


try:
    lower_limit = 10
    upper_limit = 50
    
    num = float(input("Enter a number: "))
    
    if lower_limit <= num <= upper_limit:
        print(f"The number {num} is within the range [{lower_limit},{upper_limit}].")
    else:
        print(f"The number {num} is outside the range[{lower_limit},{upper_limit}].")
except ValueError:
    print("Invalid input. Please enter a numerical value.")
except Exception as e:
    print(f"An error occured:{e}")


# ### 10.Create a Python program that determines the grade of a student based on their score using if-else

# In[45]:


try:
    # Enter the Student score
    score = float(input("Enter the student score: "))
    # check the grades based upon student score
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"The Student grade is {grade}.")
    else:
        print("Invalid inpput.Please enter the number between 0 and 100.")
except ValidError:
    print("Invalid input. Please enter a valid numeric score.")
except Exception as e:
    print("An error occured:{e}")


# ### 11.Write a Python program to check if a string is empty or not using if-else

# In[47]:


try:
    user_input = input("Enter a string:")
    
    if user_input.strip() == "":
        print("The string is empty.")
    else:
        print("The string is not empty.")
except Exception as e:
    print(f"An Error occured:{e}")


# ### 12.Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) based on input values using if-else

# In[54]:


try:
    side1 = float(input("Enter the length of First side: "))
    side2 = float(input("Enter the length of Second side: "))
    side3 = float(input("Enter the length of Third side: "))
    
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 +side3 <= side1):
        print("Invalid input. The given side lengths do not form a valid Triangle.")
    else:
        if side1 == side2 == side3:
            triangle_type = "equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            triangle_type = "isosceles"
        else:
            triangle_type = "scalene"
            
        print(f"The triangle is a {triangle_type} triangle.")
except ValueError:
    print("Invalid input. Please enter valid numeric side lengths.")
except Exception as e:
    print(f"An error occured:{e}")


# ### 13.Write a Python program to determine the day of the week based on a user-provided number using if-else

# In[58]:


try:
    day_number = int(input("Enter a number (1-7) representing the day of the week:"))
                     
    if 1 <= day_number <= 7:
        if day_number == 1:
            day = "Sunday"
        elif day_number == 2:
            day = "Monday"
        elif day_number == 3:
            day = "Tuesday"
        elif day_number == 4:
            day = "Wednesday"
        elif day_number == 5:
            day = "Thursday"
        elif day_number == 6:
            day = "Friday"
        else:
            day = "Saturday" 
        print(f"The day corresponding to {day_number} is {day}.")
    else:
        print("Invalid input. Please enter a number between 1 and 7.")
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
except Exception as e:
    print(f"An error occurred: {e}")              


# ### 14.Create a Python program that checks if a given year is a leap year using both if-else and a function

# In[59]:


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
try:
    year = int(input("Enter a year: "))
    
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input.Please enter a valid numeric year.")
except Exception as e:
    print(f"An Error occured:{e}")


# ### 15.How do you use the "assert" statement in Python to add debugging checks within if-else blocks

# In[80]:


try:
    x = 5
    num = int(input("Enter a number:"))
    if x%2 == 0:
        assert x > 0
        print("The number is positive")
    else:
            assert x < 10
            print("The number is negative")
except Exception as e:
    print(e)


# ### 16.Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else

# In[85]:


try:
    age = int(input("Enter your age:"))
    if age > 60:
        print("The person is eligible for senior citizen discount")
    else:
        print("The person is not eligible for senior citizen discount")
except Exception as e:
    print(e)


# ### 17.Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else

# In[94]:


try:
    char = input("Enter a character:")
    if len(char) != 1:
        print("Input invalid.Please Enter the correct character")
    else:
        if char.islower():
            print(f"{char}The character is lowercase character.")
        elif char.isupper():
            print(f"{char}The character is uppercase character.")
        else:
            print(f"{char} is neither uppercase nor lowercase character.")
except Exception as e:
    print(e)


# ### 18.Write a Python program to determine the roots of a quadratic equation using if-else

# In[102]:


import math
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b+math.sqrt(discriminant))/(2*a)
        root2 = (-b-math.sqrt(discriminant))/(2*a)
        print(f"Roots are real and distinct:{root1} and{root2}")
    elif discriminant == 0:
        root1 = -b/(2*a)
        print(f"Root is real and repeated:{r0ot1}")
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(abs(discriminant))/(2*a)
        print(f"Roots are real and complex:{real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")
except Exception as e:
    print(e)


# ### 19.Create a Python program that checks if a given year is a century year or not using if-else

# In[108]:


try:
    year = int(input("Enter a year:"))
    if year%100 == 0:
        print(f"The {year} is a century year.")
    else:
        print(f"The {year} is not a century year.")
except Exception as e:
    print(e)


# ### 20.Write a Python program to determine if a given number is a perfect square using if-else

# In[117]:


try:
    num = float(input("Enter a number:"))
    if num >= 0:
        sqrt = int(num**0.5)
        if sqrt**2 == num:
            print(f"{num}is a perfect square.")
        else:
            print(f"{num} is not a perfect square.")
    else:
        print(f"Please enter a non-negative number.")
except ValueError:
    print("Invalid input.Please enter the correct valid input.")
except Exception as e:
    print(e)


# ### 21.Explain the purpose of the "continue" and "break" statements within if-else loops

# In[122]:


for i in range(1,10):
    if i == 6:
        continue
    print(i)    


# In[124]:


try:
    numbers = [2,3,4,5,6,7,8,9]
    targets = 4
    for num in numbers:
        print(f"found{targets} in the list:")
        break
    print("Display the list.")
except Exception as e:
    print(e)


# #### 22.Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and height using if-else

# In[128]:


try:
    weight = float(input("Enter your weight in kilograms "))
    height = float(input("Enter your height in meters"))
    bmi = weight/(height**2)
# check weight and height based upon the bmi calculator
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normalweight"
    elif 25 <= bmi < 29.9:
        category = "overweight"
    else:
        category = "obese"
    print(f"Your BMI is {bmi:.2f}")
    print(f"Category: {category}") 
except Exception as e:
    print(e) 


# ### 23.How can you use the "filter()" function with if-else statements to filter elements from a list

# In[129]:


numbers = [1,2,3,4,5,6,7,8,9]

def filter_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
filtered_numbers = filter(filter_even, numbers)

filtered_numbers_list = list(filtered_numbers)

print(filtered_numbers_list)


# ### 24.Write a Python program to determine if a given number is prime or not using if-else

# In[132]:


num = int(input("Enter a number:"))

if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num}is a prime number")
else:
    print(f"{num} is not a prime number")


# # Map

# ### 1.Explain the purpose of the `map()` function in Python and provide an example of how it can be used to apply a function to each element of an iterable

# In[138]:


try:
    def mul(x):
        return x * 2
# Enter the list of numbers
    numbers = [1,2,3,4,5]
# use map() to apply square function to each element of list
    mul_numbers = map(mul, numbers)
# convert result to a list
    mul_numbers_list = list(mul_numbers)
    print(mul_numbers_list)
except Exception as e:
    print(e)


# ### 2.Write a Python program that uses the `map()` function to square each element of a list of numbers

# In[4]:


try:
    def square(x):
        return x**2
    numbers = [1,2,3,4,5,6]
    square_numbers = map(square, numbers)
    square_numbers_list = list(square_numbers)
    print(square_numbers_list)
except Exception as e:
    print(e)


# ### 3.How does the `map()` function differ from a list comprehension in Python, and when would you choose one over the other

# In[146]:


# Enter the list of numbers
numbers = [1, 2, 3, 4, 5]
# using list comprehension
squared_numbers = [x**2 for x in numbers]

# Print the squared numbers
print(squared_numbers)


# In[3]:


try:
    def square(x):
        return x**2
    numbers = [2,3,4,5,6]
    square_numbers = map(square, numbers)
    square_numbers_list = list(square_numbers)
    print(square_numbers_list)
except Exception as e:
    print(e)


# ### 4.Create a Python program that uses the `map()` function to convert a list of names to uppercase

# In[5]:


# Enter the list of strings
names = ["Anand","Ravi","Krish","Sudhanshu"]
# use map() to convert each name to uppercase
uppercase_number = map(str.upper, names)
# convert result to list
uppercase_number_list = list(uppercase_number)
print(uppercase_number_list)


# ### 5.Write a Python program that uses the `map()` function to calculate the length of each word in a list of strings

# In[6]:


# Enter the name of the strings
strings = ["Data","Science","Best","Career"]
# use map() to apply len()function to attach string
word_length = map(len, strings)
# convert result to list
word_length_list = list(word_length)
print(word_length_list)


# ### 6.How can you use the `map()` function to apply a custom function to elements of multiple lists simultaneously in Python

# In[8]:


try:
    def custom_fun(x,y):
        return x+y
# create two lists
    list1 = [1,2,3,4]
    list2 = [10,20,30,40]
# use map() to apply custom function to elements of both lists
    result = map(custom_fun, list1, list2)
# convert result of lists
    result_list = list(result)
    print(result_list)
except Exception as e:
    print(e)


# ### 7.Create a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit

# In[10]:


try:
    # Define function to convert celsius to fahrenheit
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) +32
    # Enter number of temperatures in celsius
    celsius_temperatures = [0, 15, 30, 45, 60]
    # use map() to apply conversion function to each temperatures
    fahrenheit_temperatures = map(celsius_to_fahrenheit, celsius_temperatures)
    # convert result to a list
    fahrenheit_temperatures_list = list(fahrenheit_temperatures)
    print(fahrenheit_temperatures_list)
except Exception as e:
    print(e)


# ### 8.Write a Python program that uses the `map()` function to round each element of a list of floating-point numbers to the nearest integer

# In[11]:


try:
    # Create list of floating numbers
    float_num = [3.14, 2.75, 6.89, 1.618]
    # use map() to round eah other to nearest integer
    rounded_num = map(round, float_num)
    # convert result to a list
    rounded_num_list = list(rounded_num)
    print(rounded_num_list)
except Exception as e:
    print(e)


# # Reduce

# ### 1.What is the `reduce()` function in Python, and what module should you import to use it? Provide an example of its basic usage
# 

# In[23]:


# define custom function to add two numbers
from functools import reduce
# create list of numbers
def custom_add(x, y):
    return x + y
try:
        numbers = [1,2,3,4,5]
        
        result = reduce(custom_add, numbers)
        print(result)
except ValueError:
    print("Invalid input.Please enter valid number of elements")


# ### 2.Write a Python program that uses the `reduce()` function to find the product of all elements in a list

# In[24]:


from functools import reduce
def custom_multiply(x, y):
    return x * y
try:
    numbers = [1,2,3,4,5]
    product = reduce(custom_multiply, numbers)
    print(product)
except ValueError:
    print("Invalid input.Please enter a valid elements in the list")


# ### 3.Create a Python program that uses `reduce()` to find the maximum element in a list of numbers

# In[25]:


from functools import reduce
# Define custom function to find maximum of two numbers
def custom_max(x,y):
    return x if x >y else y
try:
    # create list of numbers
    numbers = [1, 5, 15, 22, 50,25]
    # use reduce() to apply custom_max function
    maximum = reduce(custom_max, numbers)
    print(maximum)
except ValueError:
    print("Invalid input. Please enter a valid numbers")


# ### 4.How can you use the `reduce()` function to concatenate a list of strings into a single string

# In[18]:


from functools import reduce
    # Define concatenate function to concatenate two strings
def concatenate_strings(x, y):
    return x + y
try:
    # Enter list of strings
    strings = ["Data",",","Science","!"]
    # use reduce() to apply concatenate strings
    result = reduce(concatenate_strings, strings)
    print(result)
except ValueError:
    print("Invalid input.Please enter a valid string")


# ### 5.Write a Python program that calculates the factorial of a number using the `reduce()` function

# In[20]:


from functools import reduce
# Define factorial of two numbers
def factorial(x, y):
    return x * y
try:
    # Enter list of numbers
    num = int(input("Enter a number:"))
    numbers = list(range(1, num + 1))
    # use reduce() to apply factorial numbers
    result = reduce(factorial, numbers, 1)
    print(f"The factorial of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid input")


# ### 6.Create a Python program that uses `reduce()` to find the GCD (Greatest Common Divisor) of a list of numbers

# In[22]:


from functools import reduce
import math
# Define custom function to find gcd of the numbers
def custom_gcd(x, y):
    return math.gcd(x, y)
try:

    # create list of numbers
    numbers = [36,48,60,72]
    #use reduce() to find list fo gcd numbers
    gcd_result = reduce(custom_gcd, numbers)
    print(f"The Gcd of the numbers is {gcd_result}")
except ValueError:
    print("Invalid input. Please enter a valid input")


# ### 7.Write a Python program that uses the `reduce()` function to find the sum of the digits of a given number.

# In[27]:


from functools import reduce
# Define custom function to add two numbers
def add_digits(x, y):
    return int(x) + int(y)
try:
    # Input a number from user
    num = int(input("Enter a number: "))
    # convert number to a string to split into digits
    num_str = str(num)
    # use reduce() to find sum of digits
    digit_sum = reduce(add_digits, num_str)
    
    print(f"The sum of the digits of {num} is {digit_sum}")
except ValueError:
    print("Invalid input.Please enter a valid number.")


# # Filter

# ### 1.Explain the purpose of the `filter()` function in Python and provide an example of how it can be used to filter elements from an iterable

# In[29]:


# Define filtering function to check if number is positive
def is_positive(num):
    try:
        return num > 0
    except TypeError:
        # ahndle exceptions raised for non-numeric elements
        return False
# create a list with mixed data types, declaring non-numerical elements
data = [1,2,'three',4,'five',6]
# use filter() to filter positive numbers to handle exceptions
filtered_data = list(filter(is_positive, data))

print(filtered_data)


# ### 2.Write a Python program that uses the `filter()` function to select even numbers from a list of integers

# In[30]:


# Define a filtering function to check if number is even
def is_even(num):
    return num%2 == 0
# create list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
# use filter to select even numbers
even_numbers = list(filter(is_even, numbers))
print(even_numbers)


# ### 3.Create a Python program that uses the `filter()` function to select names that start with a specific letter from a list of strings

# In[51]:


# Enter the names in the given list
names = ["Anil","Ravi","Keshav","Sunny","Nikhil"]
# check the name to start with specific letter 
def starts_with_letter(name, letter):
    return name.startswith(letter)
try:
    # Enter the letter to filter
    letter_to_filter = input("Enter the letter to filter names: ").strip().lower()
    # check whether the filter() function is performing to select and start with specific character
    filtered_names = filter(lambda name: starts_with_letter(name.lower(), letter_to_filter),names)
    # convert filtered result to list
    filtered_names_list = list(filtered_names)
    # find how many matching letters are avialble in the list
    if filtered_names_list:
        print(f"Names starting with '{letter_to_filter}':")
        for name in filtered_names_list:
            print(name)
    else:
        print(f"No names found starting with '{letter_to_filter}'.")
except KeyboardInterrupt:
    print("\n Operation is interrupted")
except Exception as e:
    print(e)


# ### 4.Write a Python program that uses the `filter()` function to select prime numbers from a list of integers

# In[54]:


def is_prime(num):
    try:
        num = int(num)
        
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    except(ValueError, TypeError):
        return False
numbers = [2, 3, 'four', 5, 6, 'seven', 8, 9, 10, 'eleven'] 
filtered_primes = list(filter(is_prime, numbers))
print(filtered_primes)


# ### 5.How can you use the `filter()` function to remove None values from a list in Python

# In[62]:


def remove_none(value):
    try:
        # check if the value is Not none
        return value is not None
    except(ValueError, TypeError):
        # Handle Exceptions for Non-None values or types
        return False
    # create a list with different data types and None 
data = [1,2, None,'three',4, None,5,'six',None,'seven',8]
# use filter() to remove null values 
filtered_data = list(filter(remove_none, data))
print(filtered_data)


# ### 6.Create a Python program that uses `filter()` to select words longer than a certain length from a list of strings

# In[68]:


def longer_length(length):
    def filter_fun(word):
        try:
            # check whether length of word is greater than length or not
            return len(word) > length
        except(TypeError, AttributeError):
            return False
    return filter_fun
# Create a list to with different datatypes and numeric values
words = ['Data','Science',123, 'Best','Career']
min_length = 5
filtered_words = list(filter(longer_length(min_length),words))
print(filtered_words)


# ### 7.Write a Python program that uses the `filter()` function to select elements greater than a specified threshold from a list of values

# In[74]:


def greater_than_threshold(threshold):
    def filter_func(value):
        try:
            # check if value is greater than threshold
            return value > threshold
        except (TypeError, ValueError):
            # Handle the exceptions for non-numerical elements or types
            return False
    return filter_func
values = [1, 2.5, 'sachin', 4, 5]
threshold_value = 2
filtered_values = list(filter(greater_than_threshold(threshold_value), values))
print(filtered_values)


# # Recursion

# ### 1.Explain the concept of recursion in Python. How does it differ from iteration

# In[85]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    def factorial_iteration(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result   
num = 6;
print(f"The factorial of",num,"using recursion is:",factorial(6))
print(f"The factorial of",num,"using Iteration is:",factorial(6))   


# ### 2.Write a Python program to calculate the factorial of a number using recursion

# In[88]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
        # Recursive case: n! = n*(n-1)
    else:
        try:
            return n * factorial(n-1)
        except RecursionError:
            return "Recursion depth limit exceeded"
try:
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(f"The factorial of {number} is:{result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")


# ### 3.Create a recursive Python function to find the nth Fibonacci number

# In[91]:


def fibonacci(n):
    try:
        # case if n is 0 or 1, return n
        if n <= 1:
            return n
        # Recursive case: fibonacci(n)-fibonacci(n-1)+fibonacci(n-2)
        else:
             return fibonacci(n-1) + fibonacci(n-2)
    except RecursionError:
        return "Recursion depth limit exceeded"
try:
    n = int(input("Enter the value of n: "))
    result = fibonacci(n)
    print(f"The {n}th fibonacci number is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# ### 4.Write a recursive Python function to calculate the sum of all elements in a list

# In[93]:


def recursive_sum(lst):
    try:
        # Enter the length of a list
        if len(lst) == 0:
            return 0
        else:
            return lst[0] + recursive_sum(lst[1:])
    except RecursionError:
        return "Recursion depth limit exceeded"
    
try:
    user_input = input("Enter a list of numbers seperated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    
    result = recursive_sum(numbers)
    print(f"The sum of elements in the list is {result}")
except ValueError:
    print("Invalid Input.Please enter a valid list of numbers.")


# ### 5.How can you prevent a recursive function from running indefinitely, causing a stack overflow error

# In[94]:


class RecursionDepthLimitError(Exception):
    pass
def recursive_func(n, depth=0, max_depth = 100):
    if depth > max_depth:
        raise RecursionDepthLimitError("Recursion depth limit exceeded")
     
    if n == 0:
        return 0
    return recursive_func(n-1,depth + 1)
try:
    result = recursive_func(1000)
    print("Result:", result)
except RecursionDepthLimitError as e:
    print("Error:", e)


# ### 6.Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm

# In[96]:


def gcd(a, b):
    try:
        # GCD of (a, b) is 0 and GCD(a, b) = b
        if b == 0:
            return a
        # Recurseive case: GCD(a, b) = GCD(b, a%b)
        else:
            return gcd(b, a % b)
    except RecursionError:
        return "Recursion depth limit exceeded"
    
try:
    # input two numbers from user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    # calculate print and GCD using recursion and exception handling
    result = gcd(num1, num2)
    print(f"The greatest common divisor (GCD) of {num1} and {num2} is {result}")
except ValueError:
    print("Invalid input. Please enter valued integers")


# ### 7.Write a recursive Python function to reverse a string and exception handling

# In[98]:


def reverse_str(s):
    try:
        if len(s) <= 1:
            return s
        else:
            return s[-1] + reverse_str(s[:-1])
    except RecursionError:
        return "Recursion depth limit exceeded"
    
try:
    user_input = input("Enter a string: ")
    result = reverse_str(user_input)
    print(f"The reversed string is: {result}")
except Exception as e:
    print(f"Error:{e}")


# ### 8.Create a recursive Python function to calculate the power of a number (x^n)

# In[99]:


def power(x, n):
    try:
        if n == 0:
            return 1
        else:
            return x * power(x, n-1)
    except RecursionError:
        return "Recursion depth limit exceeded"
try:
    base = float(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (n): "))
    
    result = power(base, exponent)
    print(f"{base}^{exponent} is equal to {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")


# ### 9.Write a recursive Python function to find all permutations of a given string

# In[1]:


def get_permutations(s):
    try:
        if len(s) == 1:
            return [s]
        permutations = []
        for i, char in enumerate(s):
            remaining_chars = s[:i] + s[i+1:]
            sub_permutations = get_permutations(remaining_chars)
            for sub_permutation in sub_permutations:
                permutations.append(char + sub_permutation)
                
        return permutations
    except RecursionError:
        return["Recursion depth limit exceeded"]
try:
    user_input = input("Enter a string: ")
    result = get_permutations(user_input)
    
    if len(result) > 0:
        print(f"All permutations of '{user_input}':")
        for perm in result:
            print(perm)
    else:
        print("No permutations found.")
except Exception as e:
    print(f"Error:{e}")


# ### 10.Write a recursive Python function to check if a string is a palindrome

# In[2]:


def is_palindrome(s):
    try:
        if len(s) <= 1:
            return True
        elif s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    except RecursionError:
        return "Recursion depth limit exceeded"

try:
    user_input = input("Enter a string: ")
    
    cleaned_input = user_input.replace(" ", "").lower()
    
    result = is_palindrome(cleaned_input)
    if result == "Recursion depth limit exceeded":
        print("Recursion depth limit exceeded.")
    elif result:
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
except Exception as e:
    print(f"Error: {e}")


# ### 11.Create a recursive Python function to generate all possible combinations of a list of elements

# In[3]:


def generate_combinations(elements):
    try:
        # Base case: If the list is empty, return an empty list containing an empty tuple
        if not elements:
            return [()]
        
        # Recursive case: Generate combinations by including or excluding the first element
        first_element = elements[0]
        rest_of_elements = elements[1:]
        
        # Recursive call to generate combinations without the first element
        combinations_without_first = generate_combinations(rest_of_elements)
        
        # Combine the first element with combinations that exclude it
        combinations_with_first = [(first_element,) + combo for combo in combinations_without_first]
        
        # Combine both sets of combinations
        all_combinations = combinations_with_first + combinations_without_first
        
        return all_combinations
    except RecursionError:
        # Handle potential recursion depth limit exceeded exception
        return ["Recursion depth limit exceeded"]

try:
    # Input a list of elements from the user (e.g., [1, 2, 3])
    user_input = input("Enter a list of elements separated by spaces: ")
    elements = [int(element) for element in user_input.split()]

    # Generate and print all possible combinations using recursion and exception handling
    result = generate_combinations(elements)
    
    if result == "Recursion depth limit exceeded":
        print("Recursion depth limit exceeded.")
    else:
        print("All possible combinations:")
        for combo in result:
            print(combo)
except Exception as e:
    print(f"Error: {e}")


# # Basics of Functions

# ### 1.What is a function in Python, and why is it used?

# In[4]:


def greet(name):
    """A simple function that greets a person by name."""
    print(f"Hello,{name}!")
    
greet("Sachin")
greet("Sehwag")


# ### 2.How do you define a function in Python? Provide an example

# In[6]:


#define function name 
# def function_name(parameter)
def square(number):
    result = number ** 2
    return result
result = square(5)
print(result)


# ### 3.Explain the difference between a function definition and a function call

# In[8]:


# define function with parameters
def add(a, b):
    """ This function add two numbers."""
    result = a + b
    return result
# Calling the function
result = add(3,4)
print(result)


# ### 4.Write a Python program that defines a function to calculate the sum of two numbers and then calls the function

# In[9]:


# Define calculate to add two numbers
def add_numbers(a, b):
    """The function calculates the sum of two numbers."""
    result = a + b
    return result
# call function with specific values
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is {sum_result}")


# ### 5.What is a function signature, and what information does it typically include

# In[14]:


from inspect import signature
def subtraction(a:int, b:int):
    ans = a - b
    return ans

print("The answer is :", subtraction(3,10))
sig = signature(subtraction)
print(sig)
print(sig.parameters['a'])
print(sig.parameters['b'])


# ### 6.Create a Python function that takes two arguments and returns their product

# In[16]:


def multiply(a, b):
    result = a * b
    return result
num1 = 6
num2 = 5
product = multiply(num1, num2)
print(f"The multiplication product of {num1} and {num2} is {product}")


# # Function Parameters and Arguments

# ### 1.Explain the concepts of formal parameters and actual arguments in Python functions

# In[17]:


def calculate_mul(a, b):
# a and b are formal parameters
    result = a * b
    return result
result = calculate_mul(5, 6)
print(result)


# ### 2.Write a Python program that defines a function with default argument values

# In[20]:


def greet(name="Guest"):
    """This function greets a person by name, with "Guest" as default."""
    print(f"Hello, {name}!")
# calling function without providing an argument    
greet()
# calling function with argument
greet("Sachin")


# ### 3.How do you use keyword arguments in Python function calls? Provide an example

# In[21]:


def greet(name, greeting ="Hello"):
    """This function greets a person with a customizable greeting"""
    print(f"{greeting},{name}!")
    
greet(name="Alice", greeting ="Hi")
greet(greeting = "Bonjour", name = "Bob")


# ### 4.Create a Python function that accepts a variable number of arguments and calculates their sum

# In[23]:


def calculate_sum(*args):
    """Function accepts a variable number of arguments and calculates sum"""
    total = sum(args)
    return total

result = calculate_sum(5, 7, 3, 4)
print(f"The sum is:{result}")


# ### 5.What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists

# In[27]:


def addition(*num):
    sum = 0
    
    for n in num:
        sum = sum + n
    print("sum:",sum) 
addition(3, 5, 6)


# In[28]:


def intro(**data):
    print("\nData type of argument:",type(data))
    
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname = "Praveen", Lastname = "Kumar", Age = 30, phone=9768012543)
intro(Firstname = "Ravi", Lastname="sharma", Email="ravi@gmail.com", country="India")


# # Return Values and Scoping

# ### 1.Describe the role of the `return` statement in Python functions and provide examples

# In[33]:


def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_15 = create_adder(15)
print("The Result is", add_15(10))

def outer(x):
    return x * 10

def my_fun():
    return outer
res = my_fun()
print("\n the result is:",res(10))


# ### 2.Explain the concept of variable scope in Python, including local and global variables

# In[35]:


a = 1

def f():
    print('inside f():', a)
    
def g():
    a = 2
    print('Inside g():', a)
    
def h():
    global a
    a = 3
    print('Inside h():', a)
    
print('global:', a)
f()
print('global:', a)
g()
print('global:', a)
h()
print('global:', a)


# ### 3.Write a Python program that demonstrates the use of global variables within functions

# In[39]:


x = "career"

def myfun():
    x = "Science"
    print("python is "+x)
    
myfunc()
print("Python is "+x)


# ### 4.Create a Python function that calculates the factorial of a number and returns it

# In[42]:


def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        return
    elif n==0 or n==1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
    
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")


# ### 5.How can you access variables defined outside a function from within the function

# In[45]:


global_variable = 10

def access_global():
    print(f"Inside access_global:global_variable={global_variable}")
    
access_global()
print(f"After function call: global_variable = {global_variable}")


# ## Lambda Functions and Higher-Order Functions:

# ### 1.What are lambda functions in Python, and when are they typically used?

# In[52]:


is_even_list= [lambda arg=x: arg*10 for x in range(1,6)]

for item in is_even_list:
    print(item())


# In[48]:


lambda arguments: expression


# In[53]:


names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)


# In[54]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


# In[56]:


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# In[59]:


squares = lambda x: x*x
print('Using lambda: ', squares(6))


# ### 2.Write a Python program that uses lambda functions to sort a list of tuples based on the second element

# In[62]:


data = [(1,3), (2,5), (3,2), (4,6)]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)


# ### 3.Explain the concept of higher-order functions in Python, and provide an example

# In[64]:


def apply_function_to_list(func, input_list):
    result = []
    for item in input_list:
        result.append(func(item))
    return result

def square(x):
    return x ** 2

def double(x):
    return x * 2

numbers =[1, 2, 3, 4, 5]
squared_numbers = apply_function_to_list(square, numbers)
doubled_numbers = apply_function_to_list(double, numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Doubled NUmbers:", doubled_numbers)


# ### 4.Create a Python function that takes a list of numbers and a function as arguments, applying the function to each element in the list

# In[65]:


def apply_function_to_list(func, input_list):
    """Aplly given function to each element in the list"""
    result = []
    for item in input_list:
        result.append(func(item))
    return result

def square(x):
    return x**2
def double(x):
    return x*2
numbers = [1, 2, 3, 4, 5]

squared_numbers = apply_function_to_list(square, numbers)

doubled_numbers = apply_function_to_list(double, numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Doubled Numbers:", doubled_numbers)


# # Built-in Functions:

# ### 1.Describe the role of built-in functions like `len()`, `max()`, and `min()` in Python

# In[67]:


my_list =[1, 2, 3, 4, 5]
length = len(my_list)
print(length)


# In[69]:


numbers = [5, 4, 1, 2, 8]
max_values = max(numbers)
print(maximum)


# In[72]:


numbers = [5, 2, 4, 9, 3]
min_values = min(numbers)
print(min_values)


# ### 2.Write a Python program that uses the `map()` function to apply a function to each element of a list

# In[73]:


def double(x):
    return x * 2
numbers= [2, 3, 4, 5, 6]

doubled_numbers = list(map(double, numbers))

print("Original Numbers:", numbers)
print("Doubled Numbers:", doubled_numbers)


# ### 3.How does the `filter()` function work in Python, and when would you use it

# In[74]:


def is_even(x):
    return x%2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(is_even, numbers))

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)


# ### 4.Create a Python program that uses the `reduce()` function to find the product of all elements in a list

# In[76]:


from functools import reduce
# function to multiply two numbers
def multiply(x, y):
    return x * y
# list of numbers
numbers = [1, 2, 3, 4, 5]
# reduce() function to  multiply product of all elements
product = reduce(multiply, numbers)
print("Product of all elements:", product)


# # Function Documentation and Best Practices

# ### 1.Explain the purpose of docstrings in Python functions and how to write them.

# ### using triple single quotes
# ### Using triple-double quotes

# In[4]:


# using triple single quotes 
def my_function():
    '''Demonstrate triple double quotes docstrings and does nothing really.'''
    return None
print("using __doc__:")
print(my_function.__doc__)

print("using help:")
help(my_function)


# In[5]:


# using triple double quotes

def my_function():
    ' ' 'Demonstrates triple double quotes docstrings and does nothing really' ' '
  
    return None
 
print("Using __doc__:")
print(my_function.__doc__)
 
print("Using help:")
help(my_function)


# In[7]:


# Google Style Docstrings

def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.
 
    Args:
        a (int): The first number.
        b (int): The second number.
 
    Returns:
        int: The product of a and b.
    """
    return a * b
print(multiply_numbers(4,5))


# In[9]:


# Numpydoc Style Docstrings

def divide_numbers(a, b):
    """
    Divide two numbers.
 
    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.
 
    Returns
    -------
    float
        The quotient of the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
print(divide_numbers(3,6))


# In[12]:


def power(a, b):
    ' ' 'Returns arg1 raised to power arg2.' ' '
  
    return a**b
 
print(power.__doc__)


# In[14]:


# Multi-line Docstrings 
def add_numbers(a, b):
    """
    This function takes two arguments as input and given the sum as input.
    parameters:
    a(int): The first number
    b(int):The second number
    Returns:
    int: the sum of a and b.
    """
    return a + b
print(add_numbers(4, 8))


# ### Indentation in Docstrings
# The entire docstring is indented the same as the quotes in its first line.Docstring processing tools will strip a uniform amount
# of indentation from the second and further lines of the docstring, equal to the minimum indentation of all non-blank lines after 
# the first line. Any indentation in the first line of the docstring (i.e., up to the first new line) is insignificant and removed. Relative indentation of later lines in the docstring is retained. 

# In[15]:


class Employee:
    """
    A class representing an employee.
 
    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        department (str): The department the employee works in.
        salary (float): The salary of the employee.
    """
 
    def __init__(self, name, age, department, salary):
        """
        Initializes an Employee object.
 
        Parameters:
            name (str): The name of the employee.
            age (int): The age of the employee.
            department (str): The department the employee works in.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
 
    def promote(self, raise_amount):
        """
        Promotes the employee and increases their salary.
 
        Parameters:
            raise_amount (float): The raise amount to increase the salary.
 
        Returns:
            str: A message indicating the promotion and new salary.
        """
        self.salary += raise_amount
        return f"{self.name} has been promoted! New salary: ${self.salary:.2f}"
 
    def retire(self):
        """
        Marks the employee as retired.
 
        Returns:
            str: A message indicating the retirement status.
        """
        # Some implementation for retiring an employee
        return f"{self.name} has retired. Thank you for your service!"
 
# Access the Class docstring using help()
help(Employee)


# ### Docstrings in Classes
# 
# Let us take an example to show how to write docstrings for a class and the method ‘help’ is used to access the docstring

# In[16]:


class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.
 
    Attributes:
        real (int): The real part of the complex number.
        imag (int): The imaginary part of the complex number.
    """
 
    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.
 
        Parameters:
            real (int): The real part of the complex number.
            imag (int): The imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag
 
    def add(self, num):
        """
        The function to add two Complex Numbers.
 
        Parameters:
            num (ComplexNumber): The complex number to be added.
 
        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
        re = self.real + num.real
        im = self.imag + num.imag
 
        return ComplexNumber(re, im)
 
# Access the Class docstring using help()
help(ComplexNumber)
 
# Access the method docstring using help()
help(ComplexNumber.add)


# ### 2.Describe some best practices for naming functions and variables in Python, including naming conventions and guidelines.

# In[20]:


# Constants (uppercase)
MAX_VALUE = 100
PI = 3.14159

# constants (lowercase)


# Function with a descriptive name using verb-noun pairing
def calculate_total(item_prices):
    """
    Calculate the total cost of items in a list.

    Parameters:
    item_prices (list): List of item prices.

    Returns:
    float: Total cost.
    """
    total = sum(item_prices)
    return total

# Variables with descriptive names
item_prices = [10.99, 5.99, 8.49]
total_cost = calculate_total(item_prices)

# # Example 1: Calculating the area of a circle

radius = 5

pi = 3.14

area = pi * radius ** 2



# Example 2: Storing a person's information

first_name = "John"

last_name = "Doe"

age = 30


# In[ ]:




