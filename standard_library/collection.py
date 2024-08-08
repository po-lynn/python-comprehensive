from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
# Print the 3 most frequently occurring elements and their occurrence times in the words list
for elem, count in counter.most_common(7):
    print(elem, count)

mylist = [11,2,2,2,2,3,3,4,4,45,5,5]
print(Counter(mylist))

strs = 'How many times does each word show up in this sentence word show up' 
words = strs.split() #['most', 'frequently', 'occurring', 'elements']
print(words) 
print(Counter(words)) #collect total each words
#Counter({'word': 2, 'show': 2, 'up': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'in': 1, 'this': 1, 'sentence': 1})
c = Counter(words)
print(c.most_common(3)) # most common word
print(sum(c.values())) # total words
