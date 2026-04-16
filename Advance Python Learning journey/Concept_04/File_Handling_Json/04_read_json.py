import json
material = {"name":"sachin","age":19}
with open("material.json", "w") as f:
    json.dump(material,f)