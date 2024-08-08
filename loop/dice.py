import random
# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0
# for _ in range(6000):
#     face = random.randint(1, 6)
#     if face == 1:
#         f1 += 1
#     elif face == 2:
#         f2 += 1
#     elif face == 3:
#         f3 += 1
#     elif face == 4:
#         f4 += 1
#     elif face == 5:
#         f5 += 1
#     else:
#         f6 += 1
# print(f'Number Of 1. {f1} Times')
# print(f'Number Of 2. {f2} Times')
# print(f'Number Of 3. {f3} Times')
# print(f'Number Of 4. {f4} Times')
# print(f'Number Of 5. {f5} Times')
# print(f'Number Of 6. {f6} Times')


# for _ in range(6000):
#     random_number = random.randint(1,6)
#     if(random_number == 1):
#         f1 += 1
#     elif(random_number == 2):
#         f2 +=1
#     else:
#         f3 += 1
# print(f'Number of 1 {f1} times')
# print(f'Number Of 2 {f2} times')

# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1,6)
#     counters[face-1] += 1

# for face in range(1,7):
#     print(f' number of {face} time {counters[face-1]}')
range(1, 10)

items1 = [1, 2, 3, 4, 5]
items2 = [6, 7]

items3 = items1 + items2
print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]

# hello စာသားကို ထပ်ခါသုံးချင်တဲ့အခါ
items4 = ['hello'] * 3
print(items4)    # ['hello', 'hello', 'hello']

# list ထဲမှာ ရှာချင်တဲ့အခါ
print(10 in items3)        # False


# list ရဲ့ length ကို ထုတ်ကြည့်ချင်တဲ့အခါ
size = len(items3)
print(size)                 # 7

# index နဲ့ list ထဲမှ data တွေထုတ်ကြည့်ချင်တဲ့အခါ
print(items3[0], items3[-size])        # 1 1
items3[-1] = 10
print(items3[size - 1], items3[-1])    # 10 10

# 
print(items3[:5])          # [1, 2, 3, 4, 5]
print(items3[4:])          # [5, 6, 10]
print(items3[-5:-7:-1])    # [3, 2]
print(items3[::-2])        # [10, 5, 3, 1]

# list ၂ ခုကို နှိင်းယှဉ်ချြင်း
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))

print(items5 == items6)    # True
items7 = [3, 2, 1]

print(items5 <= items7)    # True

# index ကို မသုံးပြီး list ထဲမှ item တွေကို ဆွဲထုတ်နည်း
items = ['Python', 'C#', 'Javascript', 'Rust']

for item in items:
    print(item)


# list သုံးပြီး အန်စာတုန်းပုဒ်စာကို ပြန်ရေးသားနည်း
import random

counters = [0] * 6
for _ in range(5000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'No. {face} dice {counters[face - 1]} times')


print("Hello World!")


mystring="hello"
mystring[0:5:1]
mystring[0:5:-1]


