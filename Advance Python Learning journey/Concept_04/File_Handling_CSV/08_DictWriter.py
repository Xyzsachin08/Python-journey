import csv
with open("sachin_2.csv","w") as file:
    field = ["Name","Marks","City"]
    
    data = csv.DictWriter(file, field  = field)
    data.writeheader()
    
    data.writerow({
        "name": "sachin",
        "Marks":85,
        "city":"pune"
    })
    