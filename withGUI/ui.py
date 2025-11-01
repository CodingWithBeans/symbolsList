import tkinter as tk
from tkinter import filedialog as fd
from symbolsBackend import PDFPreviewer

previewer = None

def build_main_screen(root):
    global previewer


    # root creation
    root.configure(bg="#ffffff")

    # Configure grid
    for i in range(0,4):
        if i != 3: # preview row is =3
            root.rowconfigure(i, weight=0)
        else:
            root.rowconfigure(i, weight=1)
    root.columnconfigure(0, weight=1)

    #Frame creations

    welcomeFrame = tk.Frame(
        root,
        bg="#ff0000"
    )

    welcomeFrame.grid(
        row=0,
        column=0,
        pady=5
    )

    #button frame
    buttonFrame = tk.Frame(
        root,
        bg="#ffffff"
    )
    buttonFrame.grid(
        row=2,
        column=0,
        pady=10
    )

    # Scrollable preview area
    previewFrame = tk.Frame(
        root,
        bg="#cccccc"
    )
    previewFrame.grid(
        row=3,
        column=0,
        sticky="nsew"
    )

    #options frame for when user has selected a PDF
    optionsFrame = tk.Frame(
        root,
        bg="#ff0000"
    )

    optionsFrame.grid(
        row=2,
        column=1,
        pady=5
    )

    # Navigation buttons frame
    navFrame = tk.Frame(
        root,
        bg="#ffffff"
    )
    
    navFrame.grid(
        row=4,
        column=0,
        pady=5
    )


    welcomeLabel = tk.Label(
                        welcomeFrame,
                        text="Welcome to the Symbols List Extractor!",
                        font=("Segoe UI", 18, "bold"),
                        bg="#ffffff"
                    )
    
    welcomeLabel.pack(
        side="top",
        pady=20
    )

    fileLabel = tk.Label(
        root,
        text="No file selected.",
        bg="#ffffff",
        fg="#555"
    )
    fileLabel.grid(
        row=1,
        column=0,
        pady=10
    )


    selectButton = tk.Button(
        buttonFrame,
        text="Select PDF File",
        bg="#4CAF50",
        fg="white",
        command=lambda: select_file(fileLabel)
    )
    selectButton.pack(
        side="left",
        padx=5
    )

    canvas = tk.Canvas(
        previewFrame,
        bg="#eeeeee"
    )
    
    scrollbar = tk.Scrollbar(
        previewFrame,
        orient="vertical",
        command=canvas.yview
    )
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(
        side="right",
        fill="y"
    )
    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    previewer = PDFPreviewer(
        root,
        canvas
    )

    prevBtn = tk.Button(
        navFrame,
        text="◀ Prev",
        command=lambda: previewer.prev_page()
    )
    prevBtn.pack(
        side="left",
        padx=5
    )

    nextBtn = tk.Button(
        navFrame,
        text="Next ▶",
        command=lambda: previewer.next_page()
    )
    nextBtn.pack(
        side="left",
        padx=5
    )

    testbtn = tk.Button(
        optionsFrame,
        text="testbutton",
        command=None
    )

    testbtn.pack(
        side="left",
        padx=5
    )


def select_file(fileLabel):
    """Select PDF and auto-preview."""
    path = fd.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if path:
        fileLabel.config(text=f"Selected file:\n{path}")
        fileLabel.file_path = path
        previewer.load_pdf(path)  # auto-preview
    else:
        fileLabel.config(text="No file selected.")


def preview_pdf(fileLabel):
    """Load the selected PDF and show its first page."""
    path = getattr(fileLabel, "file_path", None)
    if path:
        previewer.load_pdf(path)
