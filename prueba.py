import json

f = open("MSX.json", "r")
content = f.read()
jsondecoded = json.loads(content)

name = input("Dime el nombre del juego: ")

for entity in jsondecoded:
    entityName = entity["nombre"]
    if entityName.startswith(name) is True:
        print(entityName)
        print(entity["desarrollador"])
        print(entity["id"])
