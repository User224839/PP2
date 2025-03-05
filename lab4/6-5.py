def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        file.writelines(f"{item}\n" for item in data_list)
    print(f"Data written to {filename}")

# Sample Usage
data = ["Hello", "World", "Python"]
write_list_to_file("output.txt", data)
