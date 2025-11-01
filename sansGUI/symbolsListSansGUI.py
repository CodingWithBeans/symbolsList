# puesdo code: 
# get pdf
# open it
# parse pdf
# whilst parsing need to add to lists symbols and store page number
# also need to count each symbol
# output to terminal , maybe csv if feeling fancy

#installing dependencies
from sys import exit as EXIT
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
    return answer
        
def displayOnTerminal(symbolCount, symbolPage):

    print("Symbol | Count | Pages")
    print("~" * 22)
    for symbol, count in symbolCount.most_common():
        pages = ",". join(str(pnum) for pnum in sorted(symbolPage[symbol]))
        #note pages needs 2 chara per page shown
        #bug here is the last page may have a number sliced off
        #i could for loop but thats gonna massively increase time so no.
        print(f"{symbol}   |{count}|{pages[:10]}")

def outputToCSV():
    return 0

    
def main():

    #get file path
    filePath = grabFilePath()
    #open the pdf
    pdf = openPDF(filePath)
    #parse the pdf
    symbolCount, symbolPage = parsePDF(pdf)
    #asks user what to do next
    answer = None
    while answer not in {"1", "2", "3"}:
        answer = displayOrPdf()
    #switch case depending on users choice
    system("cls")
    match answer:
        case "1":
            displayOnTerminal(symbolCount, symbolPage)
        case "2":
            outputToCSV()
        case "3":
            displayOnTerminal(symbolCount, symbolPage)
            outputToCSV()
        case _:
            EXIT("Error has occured, Exiting script")

if __name__ == "__main__":
    main()