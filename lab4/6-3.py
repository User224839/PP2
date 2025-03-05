import os

def path_info(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print(f"Path does not exist: {path}")

# Sample Usage
path_info("example.txt")
