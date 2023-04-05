input_file = open("output.txt", "r")

input_lines = input_file.readlines()
for line in input_lines:
    print(line.strip())
