def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())
    print(f"Copied contents from {source} to {destination}")

# Sample Usage
copy_file("source.txt", "destination.txt")
