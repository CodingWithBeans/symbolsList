# puesdo code: 
# get pdf
# open it
# parse pdf
# whilst parsing need to add to lists symbols and store page number
# also need to count each symbol
# output to terminal , maybe csv if feeling fancy
# will then need to go through document and check for things like GCD

#installing dependencies
import subprocess
import sys

#packages should be entered in string format. # e.g "PyMuPDF"
packages = ["PyMuPDF"]

def installdependencies(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"installing required package {package} please standby.")
    print("Packages installed, Requesting File Path from user.")

import tkinter as tk
from tkinter import filedialog as fd

def grabFilePath():
    root = tk.Tk()
    root.withdraw()

    filePath = fd.askopenfilename(
    title="Select a file",
    filetypes=[(".pdf", "*.*")]
)
    print(f"file path selected : {filePath}")


def main():
    filePath = grabFilePath()

main()
