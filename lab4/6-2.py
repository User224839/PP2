import os

def check_access(path):
    print(f"Path Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

# Sample Usage
path = "test.txt"
check_access(path)
