import pytesseract
from pdf2image import convert_from_path
import docx

def extract_text_from_image(file_path):
    from PIL import Image
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(file_path):
    images = convert_from_path(file_path)
    text = ""
    for page_image in images:
        text += pytesseract.image_to_string(page_image)
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
