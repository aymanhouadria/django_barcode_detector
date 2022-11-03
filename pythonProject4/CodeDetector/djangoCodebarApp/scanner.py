import numpy as np
from pyzbar.pyzbar import decode
import cv2
from pytesseract import pytesseract, Output
import ctypes
import ctypes.util
import os
import sys
print(len(sys.argv))
barcode = True
ocr = True
if len(sys.argv) ==2:
    if sys.argv[1] == 'barcode':
        ocr = False
    if sys.argv[1] == 'OCR':
        barcode = False



pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

run = True
cont = 0
while run:
    cont += 1
    success, img = cap.read()
    img_to_data = pytesseract.image_to_data(img)

    if barcode:
        for barcode in decode(img):
            print(barcode.data)
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts], True,(255,0,255),5)
            pts2 = barcode.rect
            cv2.putText(img, myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,(255,0,255),2)

    if ocr:
        for i, word in enumerate(img_to_data.splitlines()):
            if i != 0:
                word = word.split()
                if len(word) == 12:
                    x, y = int(word[6]), int(word[7])
                    w, h = int(word[8]), int(word[9])

                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
                    cv2.putText(img, word[11], (x, y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)
    if cont ==300:
        run = False



