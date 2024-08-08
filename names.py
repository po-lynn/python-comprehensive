note = input("Write a note ")

# with open("note.txt","a") as file:
#     file.write(f"{note}\n")
file = open("note.txt","a")
file.write(note)