import json

with open("datos.json", "r") as file:
    datos = json.loads(file)
    print(datos)