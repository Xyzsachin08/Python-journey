import json
with open("sachin.json", "r") as file:
    data = json.load(file)
    
print(data)
print(data["name"])