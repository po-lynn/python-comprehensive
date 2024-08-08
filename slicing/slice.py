year = int(input('Please enter the year: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)

#  A = π * r^2
x = 3.14159265
print(f"The value of x is {x:.2f}")

multi_string = """Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit """

mystring = "hello!"
mystring[2:] #llo
mystring[:] #hello
mystring[::] #hello
mystring[:3] # hel
mystring[1:3] # el
mystring[::2] # hlo
# Access all characters except the last one
mystring[:-1] #hello


# Access all characters except the first and last two
mystring[1:-1] #ello

mystring[::-1] # olleh


s3 = '''
hello, 
world!
'''
print(s3, end='')



s = 'abc123456'

# Forward slice operation of i=2, j=5, k=1
print(s[2:5]) # c12

# Forward slice operation of i=-7, j=-4, k=1
print(s[-7:-4]) # c12

# Forward slice operation of i=2, j=9, k=1
print(s[2:]) # c123456

# Forward slice operation of i=-7, j=9, k=1
print(s[-7:]) # c123456

# Forward slice operation of i=2, j=9, k=2
print(s[2::2]) # c246

# Forward slice operation of i=-7, j=9, k=2
print(s[-7::2]) # c246

# Forward slice operation of i=0, j=9, k=2
print(s[::2]) # ac246

# Forward slice operation of i=1, j=-1, k=2
print(s[1:-1:2]) # b135

# Negative slice operation of i=7, j=1, k=-1
print(s[7:1:-1]) # 54321c

# Negative slice operation of i=-2, j=-8, k=-1
print(s[-2:-8:-1]) # 54321c

# Negative slice operation of i=7, j=-10, k=-1
print(s[7::-1]) # 54321cba

# Negative slice operation of i=-1, j=1, k=-1
print(s[:1:-1]) # 654321c

# Forward slice of i=0, j=9, k=1
print(s[:]) # abc123456

# Forward slice of i=0, j=9, k=2
print(s[::2]) # ac246

# Negative slice of i=-1, j=-10, k=-1
print(s[::-1]) # 654321cba

# Negative slice of i=-1, j=-10, k=-2
print(s[::-2]) # 642ca