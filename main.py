import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"


def process_image(n):
    img = cv2.imread('input/' + str(n) + '.jpg')
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    img = cv2.convertScaleAbs(img, alpha=1, beta=0)
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.erode(img, kernel, iterations=8)
    img = cv2.dilate(img, kernel, iterations=6)
    img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img


def display_image(img):
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("output", 800, 1000)
    cv2.imshow("output", img)
    cv2.waitKey()
    return


def tesseract(img):
    text = pytesseract.image_to_string(img, lang="ita")
    return text


def process_text(text):
    text = text.replace("\n", " ")
    text = text.replace("\f", "\n\n")
    text = text.replace("- ", "")
    text = text.replace("  ", "\n")
    return text


def output(text):
    f = open("output/result.txt", "a")
    f.write(text)
    f.close()
    return


for i in range(64, 70):
    # display_image(process_image(i))
    output(process_text(tesseract(process_image(i))))
