# CREATING FILE HANDLERS AND MODULES FOR RETRIEVING INFO
- Create a moudle
- Open a file and load JSON data (using JSON module)
- Parse the JSON structure
- Do some calculations

## 3 FILES:
insulin.json -> the data in JSON format
json_file_handler.py -> a function to open & load any JSON file (a module)
calc_weight_json.py -> imports the module, uses the function to extract some data and perform weight calculation

## HOW TO OPEN & LOAD A JSON FILE?
with open(fileName) as alias:
     data = json.load(alias)


## USING TRY...EXCEPT TO HANDLE ERRORS