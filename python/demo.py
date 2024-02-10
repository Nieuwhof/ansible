import os

PATH = 'files'

# Create the directory
isExist = os.path.exists(PATH)
if isExist == True:
    print('Directory already exists')
else:
    os.mkdir(PATH)
    print('Directory created')

# Create 100 files
extentions = ['.txt', '.pdf', '.docx', '.xlsx', '.pptx']
for i in range(1, 101):
    file_name = f'file_{i}{extentions[i%5]}'
    with open(f'{PATH}/{file_name}', 'w') as file:
        file.write(f'This is the content of {file_name}')
        print(f'{file_name} created')   
print('All files created')




