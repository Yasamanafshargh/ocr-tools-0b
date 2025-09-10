from flask import Flask, render_template, request
from utils.ocr_utils import extract_text_from_image, extract_text_from_pdf, extract_text_from_docx
from utils.translate_utils import translate_text
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        target_lang = request.form['target_lang']
        
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Detect file type and extract text
        if file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
            extracted_text = extract_text_from_image(file_path)
        elif file.filename.lower().endswith('pdf'):
            extracted_text = extract_text_from_pdf(file_path)
        elif file.filename.lower().endswith('docx'):
            extracted_text = extract_text_from_docx(file_path)
        else:
            extracted_text = "Unsupported file format."

        # Translate the text
        translated_text = translate_text(extracted_text, target_lang)

        os.remove(file_path)  # optional: remove file after processing

        return render_template('result.html', original_text=extracted_text, translated_text=translated_text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
