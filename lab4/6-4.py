def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in {filename}: {len(lines)}")

count_lines("example.txt")