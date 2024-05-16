myFruitList=["apple", "banana", "cherry"]
print(myFruitList) # ['apple', 'banana', 'cherry']
print(type(myFruitList)) # <class 'list'>


print(myFruitList[0]) # apple
print(myFruitList[1]) # banana
print(myFruitList[2]) # cherry
# print(myFruitList[3]) # IndexError: list index out of range

# sustituimos un elemento
myFruitList[2] = "orange"
print(myFruitList) # ['apple', 'banana', 'orange']

