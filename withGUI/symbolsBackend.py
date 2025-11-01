import fitz  # PyMuPDF
from PIL import Image, ImageTk
import io

class PDFPreviewer:
    """Handles PDF rendering in a scrollable canvas."""
    
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.pdf = None
        self.page_count = 0
        self.current_page = 0
        self.images = []
        self.image_id = None

    def load_pdf(self, file_path):
        """Load PDF and render all pages as images."""

        self.pdf = fitz.open(file_path)
        self.page_count = len(self.pdf)
        self.images.clear()
        self.current_page = 0

        # Lazy load first page only
        self.render_page(self.current_page)

    def render_page(self, page_number):
        """Render a specific page."""

        page = self.pdf.load_page(page_number)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_data = Image.open(io.BytesIO(pix.tobytes("png")))
        tk_img = ImageTk.PhotoImage(img_data)

        # Store image for Tkinter
        if len(self.images) <= page_number:
            self.images.append(tk_img)
        else:
            self.images[page_number] = tk_img

        self.current_page = page_number
        self.show_page()

    def show_page(self):
        """Display the current page in the canvas."""

        img = self.images[self.current_page]
        self.canvas.delete("all")
        self.image_id = self.canvas.create_image(
            0,
            0,
            anchor="nw",
            image=img
        )
        
        self.canvas.image = img
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def next_page(self):

        if self.pdf and self.current_page < self.page_count - 1:
            self.render_page(self.current_page + 1)

    def prev_page(self):

        if self.pdf and self.current_page > 0:
            self.render_page(self.current_page - 1)
