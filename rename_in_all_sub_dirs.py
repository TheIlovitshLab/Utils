import os
import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk('Specify folder')
root.withdraw()
# Set the directory where the files are located
directory = fd.askdirectory()

# Get the strings from the user
old_string = input('Enter the old string: ')
new_string = input('Enter the new string: ')

# Use os.walk to iterate through all the files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
  # Iterate through the list of files
  for file in files:
    # Check if the old string is in the file name
    if old_string in file:
      # Get the file name and extension
      file_name, file_ext = os.path.splitext(file)
      # Replace the old string with the new string in the file name
      new_file_name = file_name.replace(old_string, new_string)
      # Create the new file path
      new_file_path = os.path.join(root, new_file_name + file_ext)
      # Rename the file
      os.rename(os.path.join(root, file), new_file_path)
