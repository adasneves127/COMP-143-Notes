# user_name = input("What is your name? ")
# print("Nice to meet you,", user_name)
# 
# user_age = input("What is your age? ")
# print("Wow", user_age, "is a cool age!")
# 
# user_major = input("What is your major? ")
# print("I love", user_major)

# Addition Calculator
# Prompt the user for 2 numbers, and print the sum
# number_one = float(input("Number 1: ")) # We use the float() function because if the user give 
# number_two = float(input("Number 2: ")) # A decimal point with the int() func, it crashes
# print(number_one + number_two)

# Scaleable -- Able to work with any size dataset, from 1 to n, where n is any positive real whole number 
number_list = [90, 70, 100, 150, 50, 75, 60]
average = sum(number_list)/ len(number_list)
print(average)
number_list.append(80)
average = sum(number_list)/ len(number_list)
print(average)

# Nonscaleable -- To add 1 number to the list, we need to change our average formula to include 4 numbers
num_1 = 90
num_2 = 70
num_3 = 100
average = (num_1 + num_2 + num_3)/ 3
print(average)
