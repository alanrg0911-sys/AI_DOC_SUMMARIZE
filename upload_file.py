from tkinter import filedialog
import pdfplumber

def upload_pdf():

    filepath = filedialog.askopenfilename(
        title = "Select a PDF.", 
        filetypes= [("PDF Files", "*.pdf")]
        )
    if not filepath.lower().endswith(".pdf"):
        print("Invalid type of file.")
    elif not filepath:
        print("No file was uploaded.")
    else:
        print("\nPDF was successfully uploaded.\n")
    
    return filepath

def extract_text(filepath):

    print("Opening PDF with pdfplumber...")

    try:
        with pdfplumber.open(filepath) as pdf:

            print(f"Number of pages: {len(pdf.pages)}")

            text = ""

            for page_number, page in enumerate(pdf.pages):
                print(f"Extracting page {page_number + 1}")

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        print("PDF extraction finished.")

        return text

    except Exception as e:
        print("Error opening PDF:")
        print(e)
        return ""