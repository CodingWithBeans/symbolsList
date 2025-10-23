# puesdo code: 
# get pdf
# open it
# parse pdf
# whilst parsing need to add to lists symbols and store page number
# also need to count each symbol
# output to terminal , maybe csv if feeling fancy

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
            symbolCount[c] += 1
            symbolPage[c].add(pageNumber)

    return symbolCount, symbolPage

def displayOrPdf():
    answer = input(f"""
                   Would you like to:
                   1) Print output to the terminal?
                   2) save output to CSV?
                   3) both?""")
    match answer:
        case "1":
            displayOnTerminal()
        case "2":
            outputToPDF()
        case "3":
            displayOnTerminal()
            outputToPDF()
        case _:
            print("Please answer either 1 or 2")
            return displayOrPdf()
        
def displayOnTerminal():
    return 0

def outputToPDF():
    return 0

    
def main():

    filePath = grabFilePath()
    pdf = openPDF(filePath)
    parsePDF(pdf)

main()
