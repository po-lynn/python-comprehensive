import json
my_dict = {
"name": "John",
"age": 30,
"isEmployed": True
}
print(json.dumps(my_dict))


import json


with open('data.json', 'w') as file:
    json.dump(my_dict, file)