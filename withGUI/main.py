import tkinter as tk
import ui

def main():
    root = tk.Tk()
    root.title("Symbols List Extractor")
    root.geometry("800x300")
    root.configure(bg="#ffffff")

    ui.build_main_screen(root)

    root.mainloop()

if __name__ == "__main__":
    main()
