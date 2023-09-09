import os
import PyPDF2

# Creating a merger
merger = PyPDF2.PdfMerger()

# Listing and sorting the files in a folder
files_list = os.listdir('C:/Users/User/Documents/Python programming/folder_to_mergepdfs')
files_list.sort()

# Merging the pdf files just if the file is .pdf extension
for file in files_list:
    if '.pdf' in file:
        merger.append(f'C:/Users/User/Documents/Python programming/folder_to_mergepdfs/{file}')

# Saving in final pdf doc
merger.write('C:/Users/User/Documents/Python programming/folder_to_mergepdfs/Final_PDF.pdf')
