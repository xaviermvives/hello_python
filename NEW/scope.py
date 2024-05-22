# the scope of a variable: a variable is only available from inside the region it is created

# local scope
def my_fun():
    x = 300
    print(x)

my_fun()
# print(x) ERROR: x is not defined

# global scope
y = 500

def second_function():
    print(y)

second_function()