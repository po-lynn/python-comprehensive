
def say_hi():
    print("Hello World")

print("Top")
say_hi()
print("Bottom")

# parameter 

def say_hi(name,age):
    print("Hello " + name + ", you are " + age)

# write one line of code

say_hi("Mike",20)
say_hi("Steve",70) 

# cube
def cube(num):
    num * num * num

cube(3) #nothing happen becuase of no return


def cube(num):
    return num * num * num
    # print("Never print it out and working it")

result = cube(4) # assign return values 

# hello("GCA")
# def hello(to="world"):
#     print("hello,",to)


# def main():
#     x = int(input("What's x?"))
#     print("x squared is", square(x))

# def square(n):
#     return n*n

# main()

# def main():
#     name = input("What's your name? ")
#     print("Hello,", hello(name))

# def hello(name):
#     return name

# main()

# def main():
#     n = int(input("Enter Num"))
#     if is_even(n):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     # return True if n%2 == 0 else False # Pythonic way
#     return n%2 == 0

# main()

def main():
    number = get_number()
    print("Number",number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n


main()

programmings = ["Python","C#","Javascript","Rust"]

print(sorted(programmings,reverse=True))



