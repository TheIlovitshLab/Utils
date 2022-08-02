import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd
import seaborn as sns

root = tk.Tk()
root.withdraw()
file_path = fd.askopenfilename()

df = pd.read_csv(file_path, skiprows=28)
hist, binedges = np.histogram(df['ECD(um)'])

xax = np.around(np.mean(np.concatenate((binedges[0:-1],binedges[1:]),axis=1),axis=1),1)
xax = np.sort(xax)
volume1 = (hist*10**4)*xax**3

plt.figure()
sns.barplot(xax, hist*10**4)
plt.xticks(
    [np.argmin(np.abs(xax-1)),
     np.argmin(np.abs(xax-2)),
     np.argmin(np.abs(xax-5)),
     np.argmin(np.abs(xax-10)),
     np.argmin(np.abs(xax-20)),
     np.argmin(np.abs(xax-50))],
    [1,2,5,10,20,50])

plt.figure()
sns.barplot(xax, volume1)
plt.xticks(
    [np.argmin(np.abs(xax-1)),
     np.argmin(np.abs(xax-2)),
     np.argmin(np.abs(xax-5)),
     np.argmin(np.abs(xax-10)),
     np.argmin(np.abs(xax-20)),
     np.argmin(np.abs(xax-50))],
    [1,2,5,10,20,50])
