# ************** Python Lists **************


# 1. Basic List Operations

numbers = [12, 4, 56, 78, 67]

print("Original List:", numbers)

# Add an element at the end
numbers.append(56)

# Add an element at a specific position
numbers.insert(1, 34)

print("Updated List:", numbers)


# Q1. Print positive and negative elements of a List.

numbers = [12, -24, 45, 67, 31, -34, -54, -34, 57]

print("\nPositive elements:")

for i in numbers:
    if i >= 0:
        print(i)

print("Negative elements:")

for i in numbers:
    if i < 0:
        print(i)


# Q2. Find the Mean (Average) of List elements.

numbers = [23, 45, 65, 47, 89, 28, 65]

total = 0

for i in numbers:
    total = total + i

average = total / len(numbers)

print(f"\nAverage = {average}")


# Q3. Find the largest element and print its index too.

numbers = [23, 45, 65, 47, 89, 28, 65, 85, 97, 35]

largest = numbers[0]
index = 0

for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
        index = i

print(f"\nLargest number = {largest}")
print(f"Index = {index}")


# Q4. Find the second greatest element.

numbers = [23, 45, 65, 47, 89, 28, 65, 85, 97, 90]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print(f"\nLargest number = {largest}")
print(f"Second largest number = {second_largest}")


# Q5. Check if List is sorted or not.

numbers = [1, 3, 4, 6, 5, 7, 8, 9]

for i in range(len(numbers) - 1):

    if numbers[i] < numbers[i + 1]:
        continue

    else:
        print("\nYour list is not sorted")
        break

else:
    print("\nYour list is sorted")                                                                                                      r                                                                                                                                                        
