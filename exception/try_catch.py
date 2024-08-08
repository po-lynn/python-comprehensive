try:
    value = 10/0 #IT will catch everyting as Invalid input
    number = int(input("Enter a number"))

except:
    print("Invalid INput")


try:
    value = 10/0 #IT will catch everyting as Invalid input
    number = int(input("Enter a number"))

except ZeroDivisionError:
    print("Divided by Zero")

except ValueError:
    print("Invalid INput")


try:
    value = 10/0 #IT will catch everyting as Invalid input
    number = int(input("Enter a number"))

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid INput")