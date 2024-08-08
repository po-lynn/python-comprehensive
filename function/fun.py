# hello("GCA")

# def hello(name):
#   print("hello,",name)


def exponent(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result


print(exponent(2, 3))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate("cat"))


# Use a star number to indicate that ARGS can receive 0 or any multiple parameters

def add(*args):
    total = 0
    # Variety parameters can be placed in the for loop and take out the value of each parameter
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


# When calling the ADD function, you can pass 0 or any multiple parameters
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

x = 25


def printer():
    x = 50
    return x


print(x)

printer()
print(x)

name = "This is a global string"


def greet():
    name = "Sammy"

    def hello():
        print("Hello" + name)

    hello()


greet()
