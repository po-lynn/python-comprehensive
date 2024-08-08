import bcrypt

# Hash a password
password = b'mysecretpassword'
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# Store the hashed password in a database
store_in_database(hashed_password)

# Check if a password matches a hash
password_to_check = b'mysecretpassword'
stored_hashed_password = get_from_database()
if bcrypt.checkpw(password_to_check, stored_hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
