# ************** For Loop **************

# Basic: Print a table of 5

for i in range(5, 51, 5):
    print(i)


# Basic: Accept a number from user and print its table

num = int(input("Enter a number: "))

for i in range(num, num * 10 + 1, num):
    print(i)


# Q1. Accept an integer and print Hello World n times.

n = int(input("Enter a number: "))

for i in range(n):
    print("Hello World")


# Q2. Print natural numbers up to n.

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)


# Q3. Reverse for loop. Print n to 1.

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)


# Q4. Take a number as input and print its table.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


# Q5. Sum up to n terms.

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print(total)


# Q6. Factorial of a number.

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"{fact} is Factorial of {n}")


# Q7. Print the sum of all even and odd numbers in a range separately.

n = int(input("Enter a number: "))

even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"Even sum = {even}")
print(f"Odd sum = {odd}")


# Q8. Print all the factors of a number.

n = int(input("Which number do you want to find factors for: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# Q9. Accept a number and check if it is a perfect number or not.
# A number whose sum of factors (excluding itself) is equal to the number itself.

n = int(input("Enter a number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total = total + i

if total == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")


# Q10. Check whether the number is prime or not.

n = int(input("Check whether your number is Prime or Not: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a Prime number")
