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


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("The result is:", result)
except ValueError:
    print("Please enter only integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Program complete.")
#The finally block will always execute, regardless of whether or not an exception was caught.
#  In this case, it simply prints "Program complete."
