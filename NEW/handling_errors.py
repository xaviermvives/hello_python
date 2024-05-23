def divide_five_by(num):
    try:
        value = 5 / num
    except ZeroDivisionError:
        print('Divide by zero error')
        value = 1
        return value
    
print(divide_five_by(2))
print(divide_five_by(0))

# print(5 / 0)