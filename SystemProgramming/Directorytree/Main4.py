import os

with os.scandir('.') as it:
    for entry in it:
        if entry.is_file():
            filepath = entry.path # absolute path
            filesize = entry.stat().st_size

print(len(path) * '---', file)

