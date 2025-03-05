import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Deleted: {path}")
        else:
            print(f"No write permission to delete {path}")
    else:
        print(f"File does not exist: {path}")

# Sample Usage
delete_file("test.txt")
