import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    """Generate a verification code of a specified length
    
    :param code_len: The length of the verification code (default 4 characters)
    :return: A random verification code string composed of uppercase and lowercase English letters and numbers
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))


# You can use the following code to generate 10 sets of random verification codes to test the above function.

for _ in range(10):
    print(generate_code()) 