from flask import Flask, request, send_from_directory
from flask import render_template as render
import ocr, os

app = Flask("__name__")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(APP_ROOT, "files")

@app.route("/")
def index():
    return render("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['imagefile']
    filename = file.filename
    imgFile = os.path.join(APP_ROOT, "files", filename)
    file.save(imgFile)
    imgFile = r""+imgFile
    return render("upload.html", answer= ocr.ocrFunction(imgFile))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
