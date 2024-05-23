# MAP

numbers = [1,2,3,4,5]

def cubic(num):
    return num **3

result = map(cubic, numbers)

print(list(result))

# ===============================
# FILTER
numbers2 = [1,2,3,5,4,5, 6,7,8]

result = filter(lambda x: x == 5, numbers2)
result2 = filter(lambda x: x > 5, numbers2)


print(list(result))
print(list(result2))

# ===============================
# REDUCE
# es necesario importar
from functools import reduce

numbers3 = [1,2,3]
result = reduce(lambda x, y: x + y,  numbers3)  # x -> accumulator
print(result) # 6

numbers4 = [1,2,3]
result4 = reduce(lambda x, y: x + y,  numbers4, 4)  # 4 -> accumulator inicial, se parte de 4 y va sumando
print(result4) # 10