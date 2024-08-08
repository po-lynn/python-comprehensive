import hashlib

# Computes the MD5 digest of the string "123456"
print(hashlib.md5('123456'.encode()).hexdigest())
import os
print(os.getcwd())  # Prints the current working directory

# Calculate the MD5 digest of the file "Python-3.7.1.tar.xz"
hasher = hashlib.md5()
import os
print(os.getcwd())  # Prints the current working directory

os.chdir('/home/po/Documents/Python/standard_library')
with open("collector.zip", 'rb') as file:
    data = file.read(512) #Data is read from the file in chunks of 512 bytes using the read() method, 
    while data:
        hasher.update(data)
        data = file.read(512)
print(hasher.hexdigest())