import os

import numpy as np
import cv2
import matplotlib.pyplot as plt
from glob import glob
import tkinter as tk
from tkinter import filedialog as fd
import tifffile as tiff

root = tk.Tk()
root.withdraw()
inpath = fd.askdirectory()

all_files = glob(inpath+'/*.tif')
if not os.path.isdir(inpath+'/filtered'):
    os.mkdir(inpath+'/filtered')

for file in all_files:
    t = tiff.imread(file)
    kernel6 = np.ones((6, 6), 'uint8')
    kernel3 = np.ones((3, 3), 'uint8')
    green_ch = t[0, :, :]
    green_ch = (green_ch - green_ch.min())/(green_ch.max()-green_ch.min())
    green_ch = (green_ch*255).astype(np.uint8)
    _, green_th = cv2.threshold(green_ch, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    conn_val = 100
    _, cc = cv2.connectedComponents(green_th, connectivity=8)

    t[0, :, :] = cv2.morphologyEx(t[0, :, :], cv2.MORPH_OPEN, kernel6)
    t[1, :, :] = cv2.morphologyEx(t[1, :, :], cv2.MORPH_OPEN, kernel3)
    tiff.imwrite(
        file.replace(inpath, inpath+'/filtered'),
        t)
