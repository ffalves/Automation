import os
from tkinter.filedialog import askdirectory

# Opening pop to choose
select_folder = askdirectory(title='Select a folder')

# Listing the documents
files_list = os.listdir(select_folder)

# Creating themes to organizer pdf's
types = {
    'images': ['.png', '.jpg'],
    'doc': ['.doc', '.docx'],
    'notes': ['.txt'],
    'sheets': ['.xlsx', '.csv', '.xlsm'],
    'pdfs': ['.pdf'],
}

# Extracting the type of file's extension
for file in files_list:
    title, extension = os.path.splitext(f'{select_folder}/{file}')
    for folder in types:
        if extension in types[folder]:
            if not os.path.exists(f'{select_folder}/{folder}'):
                os.mkdir(f'{select_folder}/{folder}')
            os.rename(f'{select_folder}/{file}',
                      f'{select_folder}/{folder}/{file}')
