import os

PATH = '/home/bertus/demo/files'

# Create the directory
isExist = os.path.exists(PATH)
if isExist == True:
    print('Directory already exists')
else:
    os.mkdir(PATH)
    print('Directory created')


#    os.mkdir(PATH)

# Create a file
#with open(os.path.join(PATH, 'file.txt'), 'w') as file: