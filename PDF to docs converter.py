from pdf2docx import Converter
pdf_file = 'Certificate of Participation - Aaradhya Patel - speedcubing.pdf'
docx_file = 'Certificate of Participation - Aaradhya Patel - speedcubing.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
