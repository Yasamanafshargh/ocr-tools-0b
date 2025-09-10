<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>OCR &amp; Translation Web App — README</title>
  <style>
    :root{
      --bg:#ffffff;
      --card:#f7f8fa;
      --accent:#0b5fff;
      --text:#111827;
      --muted:#6b7280;
      --mono:#0f172a;
    }
    body{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      color:var(--text);
      background:var(--bg);
      margin:0;
      padding:24px;
      line-height:1.6;
    }
    .container{max-width:900px;margin:0 auto;}
    header{padding:12px 0 24px;border-bottom:1px solid #e6e9ef;}
    h1{margin:0;font-size:28px;}
    .subtitle{color:var(--muted);margin-top:6px;}
    .badges img{height:20px;margin-right:8px;vertical-align:middle;}
    section{background:var(--card);padding:18px;border-radius:8px;margin-top:18px;border:1px solid #eef2f7;}
    h2{font-size:18px;margin:0 0 8px 0;}
    pre{background:#0b1220;color:#d1d5db;padding:12px;border-radius:6px;overflow:auto;font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;}
    code{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;background:#f3f4f6;padding:2px 6px;border-radius:4px;}
    ul{margin:8px 0 0 18px;}
    ol{margin:8px 0 0 18px;}
    .project-structure pre{background:transparent;color:var(--muted);padding:0;border-radius:0;}
    .two-col{display:flex;gap:20px;flex-wrap:wrap;}
    .col{flex:1 1 300px;}
    img.screenshot{max-width:100%;border-radius:6px;border:1px solid #e6e9ef;}
    footer{margin-top:22px;color:var(--muted);font-size:13px;text-align:center;}
    a{text-decoration:none;color:var(--accent);}
    @media (max-width:640px){
      body{padding:16px;}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badges" aria-hidden="true">
        <img alt="Python" src="https://img.shields.io/badge/python-3.9%2B-blue.svg" />
        <img alt="Flask" src="https://img.shields.io/badge/Flask-2.x-lightgrey.svg" />
        <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg" />
      </div>

      <h1>OCR &amp; Translation Web App</h1>
      <p class="subtitle">A web-based OCR (Optical Character Recognition) and Translation tool that extracts text from files and translates it into a target language.</p>
    </header>

    <section>
      <h2>About</h2>
      <p>
        This application allows users to upload images, PDF files, or DOCX documents, extract text using Tesseract OCR, and translate the extracted text using Google Translate (via <code>googletrans</code>).
      </p>
      <p><strong>Note:</strong> In this version, the app works best for images containing English text. Support for more languages and additional document types will be added in future releases.</p>
    </section>

    <section>
      <h2>Features</h2>
      <ul>
        <li>Extract text from images (<code>.png</code>, <code>.jpg</code>, <code>.jpeg</code>)</li>
        <li>Extract text from PDF files</li>
        <li>Extract text from DOCX files</li>
        <li>Translate extracted text into a chosen target language</li>
        <li>Simple web interface for uploading files and viewing results</li>
        <li>Lightweight and easy to deploy</li>
      </ul>
    </section>

    <section class="project-structure">
      <h2>Project Structure</h2>
      <pre>
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
      </pre>
    </section>

    <section>
      <h2>Installation</h2>

      <ol>
        <li>
          <strong>Clone the repository</strong>
          <pre><code>git clone https://github.com/yourusername/ocr-translate-app.git
cd ocr-translate-app</code></pre>
        </li>

        <li>
          <strong>Create a virtual environment (recommended)</strong>
          <pre><code>python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate</code></pre>
        </li>

        <li>
          <strong>Install dependencies</strong>
          <pre><code>pip install -r requirements.txt</code></pre>
        </li>

        <li>
          <strong>Install Tesseract OCR</strong>
          <p>Install the Tesseract engine for your platform:</p>
          <ul>
            <li><strong>Ubuntu / Debian</strong>
              <pre><code>sudo apt install tesseract-ocr</code></pre>
            </li>
            <li><strong>macOS (Homebrew)</strong>
              <pre><code>brew install tesseract</code></pre>
            </li>
            <li><strong>Windows</strong>
              <p>Download the installer from the UB Mannheim build and add the Tesseract binary to your PATH.</p>
            </li>
          </ul>
        </li>
      </ol>
    </section>

    <section>
      <h2>Usage</h2>
      <p>Start the Flask server and open the application in your browser:</p>
      <pre><code>python app.py</code></pre>
      <p>Open your browser and go to <code>http://127.0.0.1:5000</code>. Upload a file, choose the target language, and view the extracted and translated text.</p>
    </section>

    <section>
      <h2>Requirements</h2>
      <p>The following packages are required. Save these into <code>requirements.txt</code> (or use the one included in the repo):</p>
      <pre><code>fastapi
uvicorn
pytesseract
pdf2image
Pillow
python-docx
googletrans==4.0.0-rc1
jinja2
python-multipart
Flask</code></pre>
    </section>

    <section>
      <h2>Demo</h2>
      <p>Place screenshots in <code>docs/screenshots/</code>. Example image references:</p>
      <div class="two-col">
        <div class="col">
          <figure>
            <img class="screenshot" src="docs/screenshots/upload.png" alt="Upload Page screenshot" />
            <figcaption style="color:var(--muted);font-size:13px;margin-top:6px;">Upload page (placeholder)</figcaption>
          </figure>
        </div>
        <div class="col">
          <figure>
            <img class="screenshot" src="docs/screenshots/result.png" alt="Result Page screenshot" />
            <figcaption style="color:var(--muted);font-size:13px;margin-top:6px;">Result page (placeholder)</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section>
      <h2>Future Improvements</h2>
      <ul>
        <li>Improve multilingual OCR support (better accuracy for non-English text)</li>
        <li>Add support for additional formats such as <code>.txt</code> and <code>.pptx</code></li>
        <li>Enable batch file uploads</li>
        <li>Provide a Dockerfile and docker-compose setup for easy deployment</li>
        <li>Create an API version using FastAPI for programmatic access</li>
      </ul>
    </section>

    <section>
      <h2>Author</h2>
      <p>Yasaman Afshar Ghasemloo</p>
    </section>

    <section>
      <h2>License</h2>
      <p>This project is available under the <a href="#" title="Add your license link">MIT License</a> (or choose another license). Add a <code>LICENSE</code> file to the repository with the full license text.</p>
    </section>

    <footer>
      <p>Generated README — save as <code>README.html</code> or copy the content into your preferred README format.</p>
    </footer>
  </div>
</body>
</html>
