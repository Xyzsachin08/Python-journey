import json
data = {
    "name":"sachin",
    "age":19,
    "skill":["python","java"]
    }

with open("sachin.json","w") as file:
    json.dump(data,file)