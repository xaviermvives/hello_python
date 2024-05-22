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



 ###################################################
sons = ["jonhy", "mary", "jack", "peter"]

for son in sons:
    print(son, " is doing chores")

# range
for number in range(4):
    print(sons[number])

for number in range(len(sons)):
    print(sons[number])


# looping dictionaries
ages = {"john": 23, "martha":16, "peter":14, "lauren":34}
for key, value in ages.items():
    print(f'{key}:{value}')
    result = key + " is " + str(value) + " old"
    result2 = f'{key} is {value} old.'
    print(result)
    print(result2)


# while loop
rain = True
hours = 0

while rain:
    print("It's raining")
    hours += 1
    if hours == 5:
        rain = False

if rain:
    print("The floor is wet")

print("It's sunny")


# only even numbers
numbers = 0
while numbers < 10:
    numbers +=1
    if numbers%2 != 0:
        continue # if condition meets, we avoid the next lines and return to the loop
    print(numbers)

# using a for loop to add up numbers of a list
result = 0
my_numbers = [1,2,3]
for number in my_numbers:
    result += number

print(f'The sum of {my_numbers} is: {result}')

# length = len(my_numbers)  - 1
# print("Length: ", length)
total = 0
for num in my_numbers:
    if len(my_numbers)  - 1 != total:
        total += num
print("Total:" , total)

# with sum()
result2 = sum(my_numbers)
print(f'The sum of {my_numbers} is: {result2}')

