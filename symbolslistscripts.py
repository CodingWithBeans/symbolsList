# puesdo code: 
# get pdf
# open it
# parse pdf
# whilst parsing need to add to lists symbols and store page number
# also need to count each symbol
# output to terminal , maybe csv if feeling fancy
# will then need to go through document and check for things like GCD

#installing dependencies
import subprocess, sys, time, itertools

#packages should be entered in string format. # e.g "PyMuPDF"
packages = {"PyMuPDF":"fitz"}

#quick fake spinner
spinner = itertools.cycle("▖▘▝▗")

def installDependencies(packages, spinner):

    for pipCommand, importCommand in packages.items():
        try:
            print(f"importing {pipCommand}...", end="", flush=True)
            #i could while loops this but will require multi threads and honestly faking it is enough.
            for _ in range(5):
                time.sleep(0.5)
                print(f"\r Importing {pipCommand} {next(spinner)}", end="", flush=True)
            __import__(importCommand)
        except ImportError:
            print(f"\nInstalling required package: {pipCommand} please standby...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pipCommand])
    print("Packages installed.")

import tkinter as tk
from tkinter import filedialog as fd
import fitz

def grabFilePath():
    """Basic function to Open a dialogue box, whilst import works this removes bugs copy pasting filepaths"""
    root = tk.Tk()
    root.withdraw()

    filePath = fd.askopenfilename(
    title="Select a file",
    filetypes=[(".pdf", "*.*")]
)
    print(f"file path selected : {filePath}")
    return filePath

def openPDF(path):
    PDF = fitz.open(path)
    return PDF

def main():
    installDependencies(packages, spinner)
    filePath = grabFilePath()
    PDF = openPDF(filePath)
    page = PDF.load_page(0)
    print(page.get_text("text"))
    PDF.close()

main()
