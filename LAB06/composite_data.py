import csv   # module for reading another files
import copy  # module for copying data in memory RAM

# definining the dictionary
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# using a for loop to iterate the dictionary and print its items (key-value pairs)
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# defining an empty list to hold the car inventory (a list of dictionaries):
myInventoryList = []

# open the csv file, to read it and print the column names, assign values to keys, append the items to myInventoryList and print number of lines
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",") # reads the csv file
    lineCount=0
    for row in csvReader:
        if lineCount == 0: # if the file is 0 prints the titles of the tabular data
            print(f'Column names are: {", ".join(row)}') # concatenate with ", " as a separator
            lineCount+=1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}') # f' -> formate strings literals with variable values
            currentVehicle= copy.deepcopy(myVehicle) # makes a real copy of the object myVehicle / if not, we will mutate myVehicle / this operation is performance-expensive and totally avoidable
            currentVehicle["vin"] = row[0] # assign value to key
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["range"] = row[3]
            currentVehicle["year"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle) # appends the new object into the array
            lineCount += 1 # inrements the counter to pass to the next line-object
    print(f'Processed {lineCount} lines.') # prints the number of lines ( objects )

    # printing every item in the new list, with a separator between them:
    for myCarProperties in myInventoryList: # loops the array
        for key, value in myCarProperties.items(): # loop every object in the array
            print("{} : {}".format(key, value)) # prints every key and value of every propiety of the object
            print("----") # prints a separator for every pair of key-value in the object


# DISCLAIMER: spaguetti code for educational purposes (copying tabular data from an external file into a list of dictionaries)
# there are better ways to do the same