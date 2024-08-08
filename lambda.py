# add = lambda num1,num2 : num1+num2
# type(add)
# add(3,4)

# records = [
#    {'name': 'Aung Aung', 'age': 25},
#    {'name': 'Maung Maung', 'age': 30},
#    {'name': 'Su Su', 'age': 20}]
 
# def get_age(record):
#    return record['age']
 
# records.sort(key=lambda record: record['age'])
# print(records)

numbers = [1, 3, 2, 4,5]
sorted(numbers, key=lambda x: x % 2)

# This sorts the list of numbers so that all the even numbers come before the odd numbers.
mylist = []
def even(record):
    mylist.append(record %2)
    return record %2
# it will return even => 0 and odd => 1
print(sorted(numbers,key=even))
print(mylist)