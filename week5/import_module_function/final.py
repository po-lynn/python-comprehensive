import sys

from module_2 import hello
if len(sys.argv) == 2:
    hello(sys.argv[1])