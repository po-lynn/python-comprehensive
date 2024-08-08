with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# records = [
#     {'name': 'Aung Aung', 'age': 25},
#     {'name': 'Maung Maung', 'age': 30},
#     {'name': 'Su Su', 'age': 20}]

# def get_age(record):
#     return record['age']

# records.sort(key=get_age(record))
# print(records)

# import csv
# with open('students.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"],row["address"])
import csv
customerName = input("What's your name? ")
customerAddress = input("What's your address ")
with open("students.csv","a") as file:
    writer = csv.writer(file,fieldnames=["name","address"])
    writer.writerow({"name":customerName,"address":customerAddress})
    