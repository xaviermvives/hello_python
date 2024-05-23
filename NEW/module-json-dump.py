import json

datos = {"name":"juan", "age":23}

with open("dato.json", "w") as archivo:
    json.dump(datos, archivo)