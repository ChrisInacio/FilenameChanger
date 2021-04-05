#############################
# LIBRARIES
#############################
# Usage of operating system dependent functionality
import os
# Libraries to open file pick dialog
import tkinter as tk
from tkinter import filedialog

print ("-----Filename Changer (Console version)-----")

#############################
# AUXILIARY FUNCTIONS
#############################
def pickPrefix():
    data = str(input("Enter the prefix for the new files: "))
    return data

#############################
# PICK FILE
#############################
root = tk.Tk()
root.withdraw()
pickedPath = filedialog.askopenfilename() # Get the file path with the file dialog
pickedPathComponents = pickedPath.split('/', -1) # Split the file path by delimiter
filePath = pickedPathComponents.copy() # Duplicate the path to create path string variable
del filePath[-1] # Delete filename from path
filePath = '/'.join(filePath) # Add '/' between each path folder
fileName = pickedPathComponents[-1] # Get the filename
fileExtension = fileName.split('.', -1)
fileExtension = fileExtension[-1]
print('\nPath selected!')

#############################
# MAIN
#############################
prefix = pickPrefix()
files = os.listdir(filePath)

i = 1
# Opens each file and renames it to the prefix inserted + sequential number
for arrayIndex, indexContent in enumerate(files):
    # Only change names of the files that aren't named the same as the prefix
    if not(indexContent.startswith(prefix)):
        nameAssignFailedFlag = 1
        originalNameWithPath = filePath + r'/' + indexContent # Create full path to current file
        renamedNameWithPath = filePath + r'/' + prefix + str(arrayIndex+i) + r'.' + fileExtension # Create full path for renamed file
        # Run cycle until file is renamed with unique name
        while nameAssignFailedFlag == 1:
            try:
