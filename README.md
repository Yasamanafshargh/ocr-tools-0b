<!DOCTYPE html>
<html>
<head>

</head>
<body>

<h1>Image Text Detection and Translation</h1>

<p>This project detects text in images and provides translation functionality. The current version works best with <strong>English text detection</strong>, and future updates will expand support for other languages.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#example-output">Example Output</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#notes">Notes</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
</ul>

<h2 id="overview">Overview</h2>
<p>The program processes input images, extracts text using OCR (Optical Character Recognition), and optionally translates the text into other languages. It provides a simple user interface for selecting images and viewing results.</p>

<h2 id="features">Features</h2>
<ul>
    <li><strong>Text Detection</strong>: Detects text in English images with high accuracy.</li>
    <li><strong>Translation</strong>: Provides translation of detected text into other languages (future improvements planned).</li>
    <li><strong>User Interface</strong>: Easy-to-use GUI for uploading and processing images.</li>
    <li><strong>Expandable</strong>: Future versions will include improved support for Persian and other languages.</li>
</ul>

<h2 id="requirements">Requirements</h2>
<ul>
    <li><strong>Python</strong> 3.7 or higher</li>
    <li><strong>OpenCV</strong></li>
    <li><strong>Tesseract OCR</strong></li>
    <li><strong>Pillow</strong></li>
    <li><strong>Googletrans</strong> (for translations)</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
    <li>Clone the repository or download the project files.</li>
    <li>Install required dependencies:
        <pre><code>pip install opencv-python pillow pytesseract googletrans==4.0.0-rc1</code></pre>
    </li>
    <li>Install <strong>Tesseract OCR</strong>:
        <p>Download and install from: <a href="https://github.com/tesseract-ocr/tesseract">Tesseract OCR</a></p>
        <p>Make sure to add Tesseract to your system PATH.</p>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li>Run the program:
        <pre><code>python main.py</code></pre>
    </li>
    <li>Upload an image through the interface.</li>
    <li>View the detected text and its translation.</li>
</ol>

<h2 id="example-output">Example Output</h2>
<pre><code>Detected Text: Hello World
Translated Text (Persian): سلام دنیا</code></pre>

<h2 id="screenshots">Screenshots</h2>
<p>Here are some example screenshots of the application:</p>

<!-- Replace the image paths with your actual images -->
<img src="docs\screenshots\upload.png" alt="App Screenshot 1" width="600">
<img src="docs\screenshots\result.png" alt="App Screenshot 2" width="600">

<h2 id="notes">Notes</h2>
<ul>
    <li>Currently optimized for <strong>English text detection</strong>.</li>
    <li>Future updates will improve support for Persian and other languages.</li>
    <li>Ensure Tesseract OCR is correctly installed and configured on your system.</li>
</ul>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2 id="contact">Contact</h2>
<p>For questions or suggestions, please contact <a href="mailto:yafsharghasemloo@gmail.com">yafsharghasemloo@gmail.com</a>.</p>

<hr>

</body>
</html>
