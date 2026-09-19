# ************** Python Functions **************


# 1. Basic Function
def greet():
    print("Hello, Welcome to Python!")


greet()


# 2. Function with Parameters
def greet_user(name):
    print(f"Hello {name}!")


greet_user("Shahbaz")


# 3. Function with Two Parameters
def add(a, b):
    print(f"Sum = {a + b}")


add(10, 20)


# 4. Function with Return Value
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print(f"Multiplication = {result}")


# 5. Check Even or Odd using Function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(10)
print(f"The number is {result}")


# 6. Find Square of a Number
def square(num):
    return num * num


print(f"Square = {square(6)}")


# 7. Find Maximum of Two Numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b


print(f"Maximum = {find_max(25, 40)}")


# 8. Function with Multiple Parameters
def student_info(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


student_info("Shahbaz", 22, "Data Analytics")


# 9. Function with Default Parameter
def welcome(name="Student"):
    print(f"Welcome, {name}!")


welcome()
welcome("Shahbaz")


# 10. Function to Calculate Average
def calculate_average(a, b, c):
    return (a + b + c) / 3


average = calculate_average(70, 80, 90)
print(f"Average = {average}")
