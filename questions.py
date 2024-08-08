from functools import reduce
sum = reduce(
    lambda a, b: a + b>0?b:0,0
    [1, 2, -3,4]
)

print (sum)