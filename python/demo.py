
from ast import main
import os

PATH = 'files'
EXTENTIONS = ['.txt', '.pdf', '.docx', '.xlsx', '.pptx']
FAMOUNT = 11

def exist_directory():
    # Create the directory
    isExist = os.path.exists(PATH)
    if isExist == True:
        print('Directory already exists')
    else:
        os.mkdir(PATH)
        print('Directory created')
    
    return isExist

def create_files():
    # Create 100 files
    for i in range(1, FAMOUNT):
        file_name = f'file_{i}{EXTENTIONS[i%5]}'
        with open(f'{PATH}/{file_name}', 'w') as file:
            file.write(f'This is the content of {file_name}')
            print(f'{file_name} created')   
    print('All files created')

    return True


def main():
    exist_directory()
    create_files()

if __name__ == '__main__':
    main()
    





