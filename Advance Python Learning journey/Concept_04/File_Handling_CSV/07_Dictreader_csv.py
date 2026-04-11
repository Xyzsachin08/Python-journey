import csv
with open("students.csv","r") as file:
    data = csv.DictReader(file)
    
    for i in data:
        print(i)