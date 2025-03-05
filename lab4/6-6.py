import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is {filename}\n")
    print("26 text files generated.")

# Sample Usage
generate_text_files()
