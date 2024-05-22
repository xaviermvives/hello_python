# FOR EXERCISES
# Loop through the items in the fruits list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


####################################################
# In the loop, when the item value is "banana", jump directly to the next item
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)




####################################################
# Use the range function to loop through a code set 6 times
for x in range(6):
    print(x)



####################################################
# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)



 