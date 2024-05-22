# DICTIONARY EXERCISES

# use the 'get' method to print the value of 'model' key of the car dictionary:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

print(car.get("model"))

#################################################################

# Change the "year" value from 1964 to 2020
car["year"] = 2020
print(car.get("year")) # 2020

#################################################################
# Add the key/value pair "color" : "red" to the car dictionary

car["color"] = "red"
print(car)


#################################################################
# Use the pop method to remove "model" from the car dictionary
car.pop("model")
print(car)


#################################################################
# Use the clear method to empty the car dictionary
car.clear()
print(car)


#################################################################
#################################################################
# LIST EXERCISES
# Use the insert method to add "lemon" as the second item in the fruits list
fruits = [ "apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print("fruits: ", fruits)

#################################################################
# Use the remove method to remove "cherry" from the fruits list
fruits = [ "apple", "banan", "cherry"]
fruits.remove("cherry")
print(fruits)

#################################################################
# Use negative indexing to print the last item in the list
fruits = [ "apple", "banan", "cherry", "mandarina"]
print(fruits[-1])

#################################################################
# Use a range of indexes to print the third, fourth, and fifth item in the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#################################################################
# Use the correct syntax to print the number of items in the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(fruits))