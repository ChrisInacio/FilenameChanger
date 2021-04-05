# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:10:31 2021

@author: Christophe Inácio
"""
#############################
# LIBRARIES
#############################
# Usage of operating system dependent functionality
import os
# High-level operations on files
from shutil import copyfile as cpFile
# Libraries to open file pick dialog
import tkinter as tk
from tkinter import filedialog
# Library to exit a script
import sys

print ("-----Filename Changer (Console version)-----")

#############################
# INITIAZATION
#############################
# mainDirectory = os.path.dirname(os.path.realpath(__file__)) # Get current working directory
# os.chdir(os.path.dirname(os.path.realpath(__file__))) # Set current working directory

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
print('\nFile selected!')

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
                os.rename(originalNameWithPath,renamedNameWithPath)
                nameAssignFailedFlag = 0
            except:
                print('Name already taken!')
                nameAssignFailedFlag = 1
                i = i+1
                renamedNameWithPath = filePath + r'/' + prefix + str(arrayIndex+i) + r'.' + fileExtension

print('\n-----End of Program-----')