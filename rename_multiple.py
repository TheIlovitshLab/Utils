import os
import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk('Specify folder')
root.withdraw()
# Set the directory where the files are located
directory = fd.askdirectory()

# Choose the strings
old_string = input('Enter the old string: ')
new_string = input('Enter the new string: ')

# Use os.listdir to get a list of all files in the directory
files = os.listdir(directory)

# Iterate through the list of files
for file in files:
  # Check if the word "hello" is in the file name
  if old_string in file:
    # Get the file name and extension
    file_name, file_ext = os.path.splitext(file)
    # Replace the word "hello" with "goodbye" in the file name
    new_file_name = file_name.replace(old_string, new_string)
    # Create the new file path
    new_file_path = os.path.join(directory, new_file_name + file_ext)
    # Rename the file
    os.rename(os.path.join(directory, file), new_file_path)
