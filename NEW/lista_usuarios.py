user_list = [
    {"name": "john", "phone":"45456785", "age":23}, # numeros no calculables (phone...): strings (según número si es largo mucha memoria, en string no ocupa tanto)
    {"name": "mary", "phone":"47485932", "age":25}, 
    {"name": "rose", "phone":"95848533", "age":45}
    ]

user_list.append({"name": "pepi", "phone":"95848533", "age":45})
print(user_list)
print(type(user_list))
print(len(user_list)) 
print(user_list[0]["name"])

# printing capitalized name from user_list
for user in user_list:
    print(user['name'].capitalize()) 




# creating a new user with input data
name = input("What is your name? ")
phone = input("Enter your phone: ")
age = int(input("Enter your age: "))

new_user = {"name" : name, "phone" : phone, "age" : age }
print(new_user)

user_list.append(new_user)


# printing name, age, phone from every object from user_list
for user in user_list:
    print(f'{user["name"]} | {user["age"]} | {user["phone"]}') 