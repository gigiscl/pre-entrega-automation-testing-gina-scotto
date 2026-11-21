import csv
import json


def lector_users_csv():
    with open("data/users.csv", newline="") as file:
        lector = csv.DictReader(file)
        return list(lector)

def lector_productos_json():
    with open("data/productos.json") as file:
        return json.load(file)



data = lector_users_csv()
print(data)