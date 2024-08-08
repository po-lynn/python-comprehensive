import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# Find the largest three elements in a list
print(heapq.nlargest(3, list1))
# Find the smallest three elements in a list
print(heapq.nsmallest(3, list1))

list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# Find the three most expensive stocks
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# Find the three stocks with the highest number of holdings
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))