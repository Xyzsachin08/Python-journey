import csv
with open("xyz.csv","w") as file:
    write = csv.writer(file)
    
    data = [
        ["sachin","popat","Borude"], ["Onkar","Popat","Borude"],["Ganesh","Popat","Borude"]
    ]
    
    write.writerow(data)