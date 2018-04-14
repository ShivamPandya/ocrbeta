from PIL import Image
import pytesseract as ocr

def ocrFunction(imgPath):
    img = Image.open(imgPath)
    ocr.pytesseract.tesseract_cmd= "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    text = ocr.image_to_string(img, lang="eng")
    try:
        return str(eval(text))
    except:
        return text
