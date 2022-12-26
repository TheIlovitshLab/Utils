import os
import shutil
import tkinter as tk
import tkinter.filedialog as fd

# Set the source and destination directories
root = tk.Tk('Specify input folder')
root.withdraw()
src_dir = fd.askdirectory()

root = tk.Tk('Specify output folder')
root.withdraw()
dst_dir = fd.askdirectory()

# Iterate over the files in the source directory
for file in os.listdir(src_dir):
    # Construct the full file path
    src_path = os.path.join(src_dir, file)
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(src_path):
        # Create the destination folder with the same name as the file
        dst_folder = os.path.join(dst_dir, file, 'Calibration file')
        os.makedirs(dst_folder, exist_ok=True)
        # Construct the destination file path
        dst_path = os.path.join(dst_folder, file)
        # Copy the file to the destination
        shutil.copy(src_path, dst_path)
        print(f'{file} copied to {dst_folder}')
