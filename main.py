import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

def select_pdf_to_merge():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        pdf_files_listbox.insert(tk.END, pdf_file)

def remove_selected_pdf():
    selected_items = pdf_files_listbox.curselection()
    for item in reversed(selected_items):
        pdf_files_listbox.delete(item)

def select_output_directory():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

def merge_pdfs():
    pdfs = pdf_files_listbox.get(0, tk.END)
    if not pdfs:
        output_label.config(text="No PDF files selected. Nothing to merge.")
        return

    output_filename = os.path.join(output_dir_entry.get(), output_filename_entry.get())

    pdf_merger = PdfMerger()

    for pdf_file in pdfs:
        pdf_merger.append(pdf_file)

    pdf_merger.write(f"{output_filename}.pdf")
    pdf_merger.close()

    output_label.config(text=f"\t\tPDFs merged and saved as '{output_filename}'\t\t")

app = tk.Tk()
app.title("PDF Merger")

pdf_files_label = tk.Label(app, text="PDF Files to Merge:")
pdf_files_label.pack()

pdf_files_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE)
pdf_files_listbox.pack()

pdf_files_button = tk.Button(app, text="Select PDF Files to Merge", command=select_pdf_to_merge)
pdf_files_button.pack()

remove_button = tk.Button(app, text="Remove Selected", command=remove_selected_pdf)
remove_button.pack()

output_dir_label = tk.Label(app, text="Output Directory:")
output_dir_label.pack()

output_dir_entry = tk.Entry(app)
output_dir_entry.pack()

output_dir_button = tk.Button(app, text="Select Output Directory", command=select_output_directory)
output_dir_button.pack()

output_filename_label = tk.Label(app, text="Output Filename (without .pdf):")
output_filename_label.pack()

output_filename_entry = tk.Entry(app)
output_filename_entry.pack()

merge_button = tk.Button(app, text="Merge PDFs", command=merge_pdfs)
merge_button.pack()

output_label = tk.Label(app, text="")
output_label.pack()

app.mainloop()
