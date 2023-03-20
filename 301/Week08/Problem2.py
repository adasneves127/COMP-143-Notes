# Assignment Question 2:
# input into var name
# split name on -
# store split name into 2 vars
# print out hello!

name = input("Enter your name (First and last name seperated by '-'): ")
split_name = name.split('-')
first_name, last_name = split_name[0], split_name[1]
print("Nice to meet you,", first_name, last_name)
