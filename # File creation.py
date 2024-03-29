# File creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Line 1\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Hello, World!\n")
    except Exception as e:
        print(f"Error while creating the file: {e}")

# File reading and display
def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            print(file.read())
    except Exception as e:
        print(f"Error while reading the file: {e}")

# File appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Added in append mode\n")
            file.write("Line 5: Another line\n")
            file.write("Line 6: Last line added in append mode\n")
    except Exception as e:
        print(f"Error while appending to the file: {e}")

# Error handling
def handle_exceptions():
    try:
        create_file()
        append_to_file()
        read_and_display_file()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    handle_exceptions()