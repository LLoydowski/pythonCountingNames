import myFunctions

file = open("names.txt", "r")
content = file.read()

names = content.split(" ")

print(myFunctions.countElements(names))
print(myFunctions.countNames(names))
print(myFunctions.getUniqueValues(names))