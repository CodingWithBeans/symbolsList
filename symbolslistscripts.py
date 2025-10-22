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

def installDependencies(packages):
    spinner = itertools.cycle("▖▘▝▗")
    for pipCommand, importCommand in packages.items():
        try:
            print(f"importing {pipCommand}...", end="", flush=True)
            for _ in range(10):
                time.sleep(0.05)
                print(f"\r Importing {pipCommand} {next(spinner)}", end="", flush=True)
            __import__(importCommand)
        except ImportError:
            print(f"\nInstalling required package: {pipCommand} please standby...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pipCommand])
    print("Packages installed.")

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
