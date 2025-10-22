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
from os import system
import tkinter as tk
from tkinter import filedialog as fd

#packages should be entered in string format. # e.g "PyMuPDF"
packages = {"PyMuPDF":"fitz"}

#quick fake spinner
spinner = itertools.cycle("▖▘▝▗")

def permission(packages):

    answer = input(f"The Script will now attempt to install the following libraries {packages}! Do you wish to continue? [Y/N]").strip().upper()
    system('cls')
    match answer:
        case "N":
            sys.exit()
        case "Y":
            return 0
        case _:
            print("Please answer either Y or N")
            return permission(packages)
    

def installDependencies(packages, spinner):

    for pipCommand, importCommand in packages.items():
        try:
            print(f"testing import {pipCommand}...", flush=True)
            #i could while loops this but will require multi threads and honestly faking it is enough.
            for _ in range(5):
                time.sleep(0.5)
                print(f"\rImporting {pipCommand} {next(spinner)}", end="", flush=True)
            __import__(importCommand)
        except ImportError:
            print(f"\nInstalling required package: {pipCommand} please standby...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pipCommand])
    system('cls')
    print("Packages installed.")

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
    """Parse the PDF and count symbols."""
    symbolCount = {}
    symbolPage = {}

    for pageNumber in range(1, len(pdf) + 1):
        page = pdf.load_page(pageNumber - 1)
        pageText = page.get_text("text")

        for c in pageText:
            if c in symbolCount:
                symbolCount[c] += 1
            else:
                symbolCount[c] = 1

            if c not in symbolPage:
                symbolPage[c] = set()
            symbolPage[c].add(pageNumber)

    for c in symbolPage:
        symbolPage[c] = sorted(symbolPage[c])
    print(symbolCount, symbolPage)
    return symbolCount, symbolPage

def main():
    system('cls')
    permission(packages)
    system('cls')
    installDependencies(packages, spinner)
    filePath = grabFilePath()
    pdf = openPDF(filePath)
    parsePDF(pdf)

main()
