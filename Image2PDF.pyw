# Imports
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
import img2pdf
import os


class Converter:
    """
    Converts .jpeg, .jpg, .png and .bmp images into .pdf using Python module img2pdf.
    GUI build with tkinter.
    """
    def __init__(self):
        super(Converter, self).__init__()
        # Root window
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title('Image2PDF')
        self.root.configure(background='black')

        # Variables
        self.image_filepath = ""
        self.dir_filepath = ""
        self.var_text = tk.StringVar()
        self.var_text.set("Select image to convert")

        # Style Sheet
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font='Georgia 10', background='black', foreground='grey')
        self.style.map('TButton', background=[('active', 'red')])
        self.style.configure('TLabel', font='Georgia 10', background='black', foreground='grey')
        self.style.configure('TEntry', font='Georgia 10', foreground='black')

        # Widgets
        self.pdf_name_entry = ttk.Entry(width=40).grid(column=1, row=6)
        self.name_label = ttk.Label(self.root, text="New Name").grid(row=5, columnspan=3)
        self.tooltip_label = ttk.Label(self.root, textvariable=self.var_text).grid(column=1, row=8)
        self.image_browse_button = ttk.Button(text="Select Image", command=self.open_file).grid(column=1, row=1)
        self.dir_browse_button = ttk.Button(text="New Directory", command=self.open_directory).grid(column=1, row=3)
        self.convert_button = ttk.Button(text="Convert", command=self.convert_file).grid(column=1, row=7)

        # Weights table
        for c in range(3):
            self.root.columnconfigure(c, weight=1)
        for r in range(8):
            self.root.rowconfigure(r, weight=1)

    def open_file(self):
        """
        Opens a file of selected type and prints the filepath to window
        """
        file = filedialog.askopenfile(mode='r', filetypes=[("Image", ".jpeg"),
                                                           ("Image", ".png"),
                                                           ("Image", ".jpg"),
                                                           ("Image", ".bmp")])
        if file:
            filepath = os.path.abspath(file.name)
            self.image_filepath = filepath
            filepath_label = ttk.Label(self.root, text=f"File:{str(filepath)}", font='Aerial 8')
            filepath_label.grid(row=2, columnspan=3)
            self.var_text.set("Select new directory")

    def open_directory(self):
        """
        Opens directory and prints directory path to window
        """
        directory = filedialog.askdirectory()
        if directory:
            dir_path = os.path.abspath(directory)
            self.dir_filepath = dir_path
            dir_path_label = ttk.Label(self.root, text=f"File:{str(dir_path)}", font='Aerial 8')
            dir_path_label.grid(row=4, columnspan=3)
            self.var_text.set("Name file Convert")

    def get_pdf_name(self):
        """
        Gets input of entry widget and returns value pdf_name
        """
        pdf_name = self.pdf_name_entry.get()
        if pdf_name is not None:
            return pdf_name

    def convert_file(self):
        """
        Takes in filepath of image and directory and uses them to convert image to pdf
        """
        image_path = self.image_filepath
        pdf_path = self.dir_filepath + "\\" + self.get_pdf_name() + ".pdf"

        image = Image.open(image_path)
        pdf_bytes = img2pdf.convert(image.filename)

        file = open(pdf_path, "wb")
        file.write(pdf_bytes)

        image.close()
        file.close()

        self.var_text.set("Successfully converted to PDF")


if __name__ == "__main__":
    app = Converter()
    app.root.mainloop()
