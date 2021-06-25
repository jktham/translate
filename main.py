import pytesseract
import PIL
import os

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"

text = pytesseract.image_to_string(PIL.Image.open('input/0.jpg'), lang="ita")

print(pytesseract.image_to_osd(PIL.Image.open('input/0.jpg')))

f = open("output/result.txt", "a")
f.write(text)
f.close()

