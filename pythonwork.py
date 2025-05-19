import json

data = { 
    "name": "paul george", 
    "age": 35,
    "team": "Philadelphia 76ers",
    "All-Star": 9, 
    "All-NBA Team": 6, 
    "injured": True
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)


print("Data has been written to data.json")
   