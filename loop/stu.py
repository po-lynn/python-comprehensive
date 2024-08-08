import random
count= {1:0,2:0,3:0,4:0,5:0,6:0}
for g in range(5000):
    roll = random.randint(1,6)
    count[roll-1] += 1

for point, count in count.items():
    print(f'no{point} times {count}')