# variable with a value of type string
myString = "This is a string"
print(myString)

print(type(myString)) # <class 'str'>

print(myString + " is of the data type " + str(type(myString)))

# string concatenation
firstString="water"
secondString="fall"
thirdString= firstString + secondString
print(thirdString) # waterfall


# input 
name = input("What is your name?")

print(name)

# format output strings
color=input("What is your favorite color? ")
animal=input("What is your favorite animal? ") 
print("{}, you like a {} {}!".format(name, color, animal))