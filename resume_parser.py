import os
import PyPDF2
import docx2txt

def extract_text_from_file(file_path):
    text = ""
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    return text
