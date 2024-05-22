# FUNCTION EXERCISES


####################################################
# Create a function named my_function
def my_function():
    print("Hello from a function")

my_function()


####################################################
# 
def greetings(name):
    print("Hello",name)
    print(f'Hello {name}')
    print("Hello {}".format(name))
    print("Hello " + name + ".")

greetings("Pepe")

####################################################
# arbitrary arguments with '*args'

def youngest_brother(*bro):
    print(f'The youngest brother is {bro[2]}')

youngest_brother("Emil", "Tobias", "Linus", "Karl") # passing a tupla as arguments

####################################################
# passing key-value pairs as arguments
def richest_user(user1, user2, user3):
    print(f'The richest user is {user3}')

richest_user(user1 = "Emil", user2 = "Tobias", user3 = "Linus")



####################################################
# Create a function that converts feet into meters: 1 meter = 3.28084 feet
def feet_to_meter(feet):
    return feet / 3.28084

five_feet_to_meter = feet_to_meter(5)
print(round(five_feet_to_meter, 3))

####################################################
# default argument
def my_country(country = "Norway"):
    print(f'I am from {country}')

my_country('Catalonia')
my_country()


####################################################
# passing a list as an argument
def my_cars(cars):
    for car in cars:
        print(car)

my_cars(['Mustang', 'Volvo', 'Porshe', 'Seat'])


####################################################
#returning values

def multiply_by_five(number):
    return 5 * number

print(multiply_by_five(2))
print(multiply_by_five(5))


####################################################
#recursion: a defined function can call itself
def countdown_from(number):
    if(number >= 0):
        print(number)
        countdown_from(number - 1)
print("Recursion example")
countdown_from(6)
countdown_from(3)
countdown_from(0)
countdown_from(-3)

# refactored to avoid 0 and negative numbers as arguments
def countdown_from2(number):
    if number == 0 or number < 0:
        print("0 or negative numbers not permitted")
    else:
        print(number)
        countdown_from(number - 1)

countdown_from2(0)
countdown_from2(-10)
countdown_from2(5)


####################################################
# function to convert dollars to euros: 1 dollar = 0.92 euros
def dollar_to_euro(quantity_in_dollars):
    return quantity_in_dollars * 0.92

result = print(f'{round(dollar_to_euro(49), 2)} euros')
