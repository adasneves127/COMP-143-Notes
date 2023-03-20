# For Loops (Definite Loops)

# Question: What are the main components to making a for loop?
# Hint: Keyword, Iteration Variable, 'in', collection of items

# Answer:
for number in range(10):
    pass

# Task: Create a loop that prints out the numbers 1-10 (Inclusive)
# Code:
for number in range(1, 11):
    print(number, end=", ")
print()

# Task: Create a loop that prints multiples of 3 from 0 to 200:
# Code:
for number in range(198, -1, -3):
    print(number, end="\t")

# Task: Create a list with numbers from 0-10. Then, in another loop, calculate the sum of the numbers, and print it out.
# Code:
numbers = []
for i in range(10):
    numbers.append(i)

list_sum = 0

for num in numbers:
    list_sum += num
print("The sum is:", list_sum)

# Task: Modify this code to take 10 user inputs, and calculate that sum.
# Code:

numbers = []
for i in range(10):
    user_num = int(input("Enter a number: "))
    numbers.append(user_num)


list_sum = 0

for num in numbers:
    list_sum += num
print("The sum is:", list_sum)



print()
