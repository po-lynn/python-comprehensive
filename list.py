# for _ in [0,1,2]:
#     print("hello")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[2:8:2]  # [3, 5, 7]

# items = ['Python', 'C#', 'Javascript', 'Rust']

# for index in range(len(items)):
#     print(items[index])




my_tuple = (1, "hello", 3.14)
my_tuple[1] # hello
# for item in items:
#    print(item)
my_dict = {'name': 'Maung Maung', 'age': 25, 'city': 'Hlaing'}

my_dict["name"]
my_dict['gender'] = 'male'
my_dict["gender"]
my_dict['age'] = 30

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
    range(start, stop, step)
my_dict = {}
# for variable in sequence:
#     # code to execute for each item in sequence
for i in xrange(0, 10, 2):
    print(i) # 0 2 4 6 8


# list ၂ ခုကို နှိင်းယှဉ်ခြင်း
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))

print(items5 == items6)    # True


# person = {
# "name": "John Doe",
# "age": 35,
# "city": "New York"
# }
# dict_length = len(person)
# print(dict_length)

# for _ in range(3):
#    print("hello")

# for i in range(10000000):
#     print(i)

# Create an empty dictionary
my_dict = {}
# Add some key-value pairs to the dictionary
my_dict['name'] = 'Maung Maung'
my_dict['age'] = 22

# name = my_dict['name']

# # Get a list of tuples containing the key-value pairs in the dictionary
# items = my_dict.items()

# # Print the key-value pairs
# for key, value in items:
#     print(key, value)

# Get a list of all the keys in the dictionary
# keys = my_dict.keys()

# Get a list of all the values in the dictionary
# values = my_dict.values()

# Print the keys and values
# for key in keys:
#     print(key, my_dict[key])

# for value in values:
#     print(value)

# customers = ["Customer1","Customer2","Customer3","Customer4"]
# cities = ["Hlaing","Alone","South Okkalar","Sanchaung"]


customers = {
   "Customer1": "Hlaing",
   "Customer2": "Alone",
   "Customer3": "South Okkalar",
   "Customer4": "Sanchaung"
}

for customer in customers:
   print(customer, customers[customer])


customes = [
   {
      "name":"Customer1","phone":"09111111111","email":"customer1@email.com","township":"Hlaing"
   },
   {
      "name":"Customer2","phone":"09222222222","email":"customer2@email.com","township":"Alone"
   },
   {
      "name":"Customer3","phone":"09333333333","email":"customer3@email.com","township":"South Okkalar"
   },
   {
      "name":"Customer4","phone":"09444444444","email":"customer4@email.com","township":"Sanchaung"
   }
]

s1 = "Hello" + ' ' + "World"
s2 = "Hello" * 2

s2 += "!"


ord("A") # 65

string1 = "apple"
string2 = "banana"

if string1 < string2:
    print(f"{string1} comes before {string2}")
else:
    print(f"{string2} comes before {string1}")


ab = "ab"
ac = "ac"
ab < ac #True


