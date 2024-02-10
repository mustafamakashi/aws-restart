#Introduction to string data type

myString = "This is a String."

print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

firstString = "Water"
secondString = "fall"

thirdString = firstString + secondString

print(thirdString)

print(firstString+secondString)

#taking input from user

name = input("What is your name? ")

print(name)


color = input("What's your favorite color? ")
animal = input("What's your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))