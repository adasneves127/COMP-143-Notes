import json

file = open("test.json")
print(json.load(file))
file.close()