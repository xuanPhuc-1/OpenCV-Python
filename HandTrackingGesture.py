import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from pynput.keyboard import Key, Controller
from pynput import keyboard

keyboardController = Controller()
#######################
wCam, hCam = 640, 480
#######################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw= False)
    if len(lmList) != 0:
        #print(lmList[0], lmList[12])

        x1, y1 = lmList[0][1], lmList[0][2]
        x2, y2 = lmList[12][1], lmList[12][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2),(255,0,255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length =  math.hypot(x2-x1,y2-y1)
        print(length)

        if length < 100:
            keyboardController.press(Key.left)
            keyboardController.release(Key.left)
        elif length >= 100:
            keyboardController.press(Key.right)
            keyboardController.release(Key.right)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("IMG",img)
    cv2.waitKey(1)