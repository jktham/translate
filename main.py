import pytesseract
import PIL

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"

print(pytesseract.image_to_string(PIL.Image.open('input/test.png'), lang="eng"))
