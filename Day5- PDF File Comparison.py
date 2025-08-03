import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()
def compare_pdfs(file1, file2):
    text1 = extract_text_from_pdf(file1)
    text2 = extract_text_from_pdf(file2)
    ratio = SequenceMatcher(None, text1, text2).ratio()
    percentage = round(ratio * 100, 2)
    if percentage == 100:
        print("✅ These PDF files are identical.")
    else:
        print(f"⚠️ These PDF files are {percentage}% similar (not identical).")
    print("\n🔍 File 1 preview:\n", text1[:300])
    print("\n🔍 File 2 preview:\n", text2[:300])
# File picker UI
root = tk.Tk()
root.withdraw()
file1 = filedialog.askopenfilename(title="Select the first PDF")
file2 = filedialog.askopenfilename(title="Select the second PDF")
compare_pdfs(file1, file2)
