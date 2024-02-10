import os
import logging

PATH = "files"  # Adjust if necessary
EXTENTIONS = [".txt", ".pdf", ".docx", ".xlsx", ".pptx"]
DEFAULT_FILE_COUNT = 100

def exist_directory():
    """Checks if the directory exists and creates it if necessary.

    Returns:
        bool: True if the directory exists or was created, False otherwise.
    """

    logger = logging.getLogger(__name__)

    # Ensure directory creation using a loop with error handling
    while not os.path.exists(PATH):
        try:
            os.mkdir(PATH)
            logger.info("Directory created:", PATH)
            return True
        except (OSError, PermissionError) as e:
            logger.error(f"Error creating directory: {e}")
            error_choice = input("Directory creation failed. Retry? (Y/N): ").lower()
            if error_choice not in ("y", "yes"):
                return False  # Respect user decision to stop

    else:
        logger.info("Directory already exists:", PATH)
        return True

def create_files(count=DEFAULT_FILE_COUNT):
    """Creates the specified number of files with appropriate extensions.

    Args:
        count (int, optional): The number of files to create. Defaults to 100.

    Returns:
        int: The actual number of files created.
    """

    if not exist_directory():
        return 0  # Indicate failure on directory creation error

    logger = logging.getLogger(__name__)
    file_count = 0
    error_count = 0

    for i in range(1, count + 1):
        file_name = f"file_{i}{EXTENTIONS[i % 5]}"
        file_path = os.path.join(PATH, file_name)

        try:
            with open(file_path, "w") as file:
                file.write(f"This is the content of {file_name}")
                logger.info(f"{file_name} created")
                file_count += 1
        except (IOError, PermissionError) as e:
            error_count += 1
            logger.error(f"Error creating {file_name}: {e}")

    if error_count > 0:
        logger.info(f"Finished with {error_count} errors.")
    else:
        logger.info(f"All {file_count} files created successfully.")

    return file_count

def main():
    """Handles user input and calls appropriate functions."""

    logging.basicConfig(level=logging.INFO)  # Set basic logging

    create_dir = input("Create the base folder for test files? (Y/N): ").lower() == "y"
    if create_dir:
        exist_directory()

    create_files_flag = input("Create test files? (Y/N): ").lower() == "y"
    if create_files_flag:
        while True:
            try:
                file_count = int(input("How many files do you want to create? (1-101): "))
                if 1 <= file_count <= 101:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 101.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        create_files(file_count)

if __name__ == "__main__":
    main()
