def get_suffix(filename, ignore_dot=True):
    """Get the suffix of the file name
    
    :param filename: file name
    :param ignore_dot: Whether to ignore the dot before the suffix name
    :return: file extension
    """
    # Reverse lookup from the string. The position where it appears
    pos = filename.rfind('.')
    # Extract the suffix from the file name by slicing
    if pos <= 0:
        return ''
    return filename[pos + 1:] if ignore_dot else filename[pos:]


print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #

help(get_suffix)

from os.path import splitext

help(splitext)

def get_suffix(filename, ignore_dot=True):
    return splitext(filename)[1][1:]

print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #
