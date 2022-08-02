import tkinter as tk
from tkinter import filedialog as fd
import tifffile as Tiff
import numpy as np


def load_2_channel_tiff() -> np.ndarray:
    """
    load a 2 channel tiff file with a tkinter filedialog
    :return: 3 channel image with zeros in blue channel
    """
    root = tk.Tk()
    root.withdraw()

    file_path = fd.askopenfilename()
    im = Tiff.imread(file_path).astype(np.uint8)
    im_rgb = np.concatenate([im,np.zeros((1,im.shape[1],im.shape[2]))],0);
    return np.moveaxis(im_rgb,0,2)

