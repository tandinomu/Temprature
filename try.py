import PyPDF2

def pdf_to_text(input_pdf, output_text):
    try:
        pdf_file = open(input_pdf, 'rb')

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
           
            text += page.extract_text()

        pdf_file.close()

        with open(output_text, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        print(f"PDF to text conversion successful. Text saved to {output_text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_pdf = "/home/tandinomu/Desktop/སྙན་ཞུ།.pdf"  
    output_text = "/home/tandinomu/Desktop/སྙན་ཞུ།.docx"  
    pdf_to_text(input_pdf, output_text)