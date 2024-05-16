# you can mix data types in a Python list

myMixedTypeList= [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# using a for statement to traverse the list and print the data type

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
