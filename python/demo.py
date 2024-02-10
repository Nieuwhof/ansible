import os

def create_directory(directory_name):
    while True:
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
            return  # Exit the loop if creation succeeds
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except OSError as e:
            print(f"Error creating directory: {e}")
        choice = input("Directory creation failed. Retry? (Y/N): ").lower()
        if choice not in ("y", "yes"):
            return  # Respect user decision to stop

def create_files(directory_name, file_extension, num_files):
    for i in range(1, num_files + 1):
        file_name = f"filenumber-{i}.{file_extension}"
        file_path = os.path.join(directory_name, file_name)
        with open(file_path, 'w') as file:
            file.write(f"This is file number {i} with extension {file_extension}")
        print(f"File '{file_name}' created successfully.")

def delete_file(directory_name, file_name):
    file_path = os.path.join(directory_name, file_name)
    try:
        os.remove(file_path)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Input validation and directory creation
while True:
    directory_name = input("Enter the name of the directory to create (or 'q' to quit): ").strip()
    if directory_name == "q":
        break  # Exit the program if the user enters 'q'
    if directory_name:
        create_directory(directory_name)
        break  # Exit the loop if directory creation succeeds
    else:
        print("Empty directory name. Please try again.")

if os.path.exists(directory_name):
    # Input validation for file creation
    while True:
        try:
            num_files = int(input("Enter the number of files to create: "))
            if num_files > 0:
                break
            else:
                print("Invalid number of files. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    file_extension = input("Enter the file extension (pdf, txt, jpg): ").lower()
    if file_extension in ("pdf", "txt", "jpg"):
        create_files(directory_name, file_extension, num_files)
    else:
        print("Invalid file extension. Please choose from pdf, txt, or jpg.")

    # Get file name for deletion
    file_name = input("Enter the name of the file to delete (including extension): ")
    delete_file(directory_name, file_name)
