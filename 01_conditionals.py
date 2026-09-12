# Q1. Accept two numbers and print the greatest between them.
num1 = int(input("Please tell your first number: "))
num2 = int(input("Please tell your second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both the numbers are same")


# Q2. Accept gender from the user and print greeting message.
gender = input("Enter your gender (M or F): ")

if gender.upper() == 'M':
    print("Good morning Sir")
elif gender.upper() == 'F':
    print("Good morning Mam")
else:
    print("Invalid input")


# Q3. Check whether an integer is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")


# Q4. Check if the user is a valid voter.
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

if age >= 18:
    print(f"Hello {name}, your age is {age}, so you are a valid Voter")
else:
    print(f"Hello {name}, your age is {age}, so you are Not a valid Voter")


# Q5. Check if a year is a leap year or not.
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is Not a leap year")


# Q6. Temperature classification.
temp = int(input("Enter Temperature: "))

if temp <= 0:
    print(f"{temp}°C - Freezing Cold")
elif 0 < temp <= 10:
    print(f"{temp}°C - Very Cold")
elif 10 < temp <= 20:
    print(f"{temp}°C - Cold")
elif 20 < temp <= 30:
    print(f"{temp}°C - Pleasant")
elif 30 < temp <= 40:
    print(f"{temp}°C - Hot")
else:
    print(f"{temp}°C - Very Hot")
