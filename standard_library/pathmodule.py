import os


path = '/home/po/Documents/Python/standard_library/collector.zip'
print(os.path.getatime(path))
print(os.path.getsize(path))
if os.path.exists(path):
    print(f'The file {path} exists.')
else:
    print(f'The file {path} does not exist.')
