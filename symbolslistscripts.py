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
    """Honestly look at the name to work out what it does this docustring is longer than the function"""
    pdf = fitz.open(path)
    return pdf

def parsePDF(pdf):
    """parse the pdf"""
    #counters page will return a list
    symbolCount = 0
    symbolPage = []

    for pageNumber in range(1, (len(pdf) + 1)):
        page = pdf.load_page(pageNumber - 1)
        pageText = page.get_text("text")
        for c in pageText:
            #testing for = sign will need a regex later
            if c == "=":
                #if we find = sign up the counters
                symbolCount += 1
                symbolPage.append(pageNumber)
        print(f"Count for = : {symbolCount} and appears on pages: {symbolPage}")
        sys.exit

def main():
    installDependencies(packages, spinner)
    filePath = grabFilePath()
    pdf = openPDF(filePath)
    parsePDF(pdf)

main()
