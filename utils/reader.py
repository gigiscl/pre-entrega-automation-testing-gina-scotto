import csv
import json


def lector_users_csv():
    with open("data/users.csv", newline="") as file:
        lector = csv.DictReader(file)
        return list(lector)


data = lector_users_csv()
print(data)