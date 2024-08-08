"""import module1
import module2

# import module1 as m1
# import module2 as m2

# The "module name. Function name" method (completely limited name) calls the function,

module1.greet()    # Hello, World!
module2.greet()     # Goodbye, World!
"""
from module1 import greet

greet()    # Hello, World!

from module2 import greet

greet()    # Goodbye, World!


from module2 import greet as f1
from module1 import greet as f2

f1()    #Goodbye, World!
f2()    #Hello, World!

