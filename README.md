OCR & Translation Web App

A web-based OCR (Optical Character Recognition) and Translation tool that allows users to upload images, PDFs, or DOCX files, extract their text content, and translate it into a target language.

Built with Flask, it uses Tesseract OCR for text extraction and Google Translate API for translations.

Note: In this version, the app works best for images containing English text. Support for more languages and document types will be added in future versions.

Features

Extract text from images (.png, .jpg, .jpeg)

Extract text from PDF files

Extract text from DOCX files

Translate extracted text into any target language

Simple web interface for uploading files and viewing results

Lightweight & easy to deploy

Project Structure
.
├── app.py                  # Main Flask app
├── utils/
│   ├── ocr_utils.py        # OCR extraction logic
│   ├── translate_utils.py  # Translation helper
├── templates/
│   ├── index.html          # Upload page
│   ├── result.html         # Result page
├── uploads/                # Temporary storage for uploaded files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Installation

Clone the repository

git clone https://github.com/yourusername/ocr-translate-app.git
cd ocr-translate-app


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Install Tesseract OCR

Ubuntu/Debian:

sudo apt install tesseract-ocr


Mac (Homebrew):

brew install tesseract


Windows:
Download the installer
 and add it to your PATH.

Usage

Run the Flask server:

python app.py


Open in your browser:

http://127.0.0.1:5000


Upload a file → Select target language → Get extracted & translated text.

Requirements
fastapi
uvicorn
pytesseract
pdf2image
Pillow
python-docx
googletrans==4.0.0-rc1
jinja2
python-multipart
Flask

Demo




Future Improvements

Better multilingual OCR support (non-English text)

Add support for .txt and .pptx files

Enable batch file uploads

Deploy with Docker

Provide an API version with FastAPI

Author

Yasaman Afshar Ghasemloo
