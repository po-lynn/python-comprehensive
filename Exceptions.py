# try:
#     # open a file
# except FileNotFoundError:
#     # exceptions handling



# while True:
#     try:
#         num = 
#         break
#     except ValueError:
#         pass


def main():
    num = get_number()
    print(f"Number is {num}")


def get_number():
    while True:
        try:
           return int(input("Please enter a valid number "))
        except:
            pass

main()