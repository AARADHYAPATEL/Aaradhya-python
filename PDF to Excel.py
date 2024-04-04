import os
from PyPDF2 import PdfReader
import pandas as pd


def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            text += page_text
    return text


def pdf_to_excel(pdf_file, output_file):
    text = pdf_to_text(pdf_file)
    lines = text.split('\n')
    df = pd.DataFrame(lines, columns=['Text'])
    df.to_excel(output_file, index=False)


# Example usage:
pdf_file = "Certificate of Participation - Aaradhya Patel - speedcubing.pdf"
output_excel_file = "Certificate of Participation - Aaradhya Patel - speedcubing.xlsx"

pdf_to_excel(pdf_file, output_excel_file)

