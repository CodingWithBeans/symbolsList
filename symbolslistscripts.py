# puesdo code: 
# get pdf
# open it
# parse pdf
# whilst parsing need to add to lists symbols and store page number
# also need to count each symbol
# output to terminal , maybe csv if feeling fancy
# will then need to go through document and check for things like GCD

#installing dependencies
from os import system
import tkinter as tk
from tkinter import filedialog as fd
from collections import defaultdict, Counter
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
    symbolCount = Counter()
    symbolPage = defaultdict(set)

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

    print("----" * 20)
    print(symbolCount)
    print("----" * 20)
    print(symbolPage)
    return symbolCount, symbolPage

def main():

    filePath = grabFilePath()
    pdf = openPDF(filePath)
    parsePDF(pdf)

main()
