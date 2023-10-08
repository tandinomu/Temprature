from reportlab.pdfgen import canvas

def text_to_pdf(input_text, output_pdf):
    c = canvas.Canvas(output_pdf)
    text = open(input_text).read()
    c.drawString(100, 750, text)
    c.save()

text_file = "/home/tandinomu/Desktop/སྙན་ཞུ།.docx"
pdf_file = "/home/tandinomu/Desktop/སྙན་ཞུ།.pdf"
text_to_pdf(text_file, pdf_file)

