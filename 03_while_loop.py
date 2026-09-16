# ************** While Loop **************

# Basic while loop

a = 1

while a <= 30:
    print(a)
    a = a + 1


# Q1. Separate each digit of a number and print it on a new line.

a = int(input("Enter a number: "))

while a > 0:
    print(a % 10)
    a = a // 10


# Q2. Accept a number and print its reverse.

a = int(input("Enter a number: "))

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)


# Q3. Accept a number and check if it is a palindromic number.
# If number and its reverse are equal, it is a palindrome.

a = int(input("Enter a number: "))

copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)

if copy == rev:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")


# Q4. Create a random number guessing game with Python.

import random

num = random.randint(1, 20)
tries = 0

while True:

    guess = int(input("Please guess your number: "))

    if num == guess:
        tries += 1
        print(f"You are right! You guessed the number in {tries} tries.")
        break

    elif num < guess:
        print("Go a little lower")
        tries += 1

    elif num > guess:
        print("Go a little higher")
        tries += 1
