from pathlib import Path

for path in Path('.').iterdir():
    info = path.stat()
    print(info.st_mtime)