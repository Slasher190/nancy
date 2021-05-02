import mouse
import HandTrackingModule as hmt
import numpy as np
import cv2
import math
import pyautogui as pgi

detector = hmt.handDetector(detectionCon=0.7)
hCam = 1080
wCam = 1920
# print(mouse.get_position()) #initial(0,0) final(1920,1080)
# mouse.drag(0,0,1280,720,duration=1)



cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
x1,y1 = 0,0
# print(pgi.size())
while True:
    success,img1 = cap.read()
    img = cv2.flip(img1,1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
        x1,y1 = lmlist[8][1],lmlist[8][2]
        x2,y2 = lmlist[12][1],lmlist[12][2]
        x3,y3 = lmlist[4][1],lmlist[4][2]
        length = math.hypot(x2-x1,y2-y1)
        mouse.move(x1,y1) #fast
        # print(mouse.get_position(),x1,y1)
        if (length < 40):
            mouse.click()
        # print(length)
        # pgi.moveTo(x1,y1)  #too slow
        
        # x1,y1 = x2,y2
    # cv2.namedWindow('IMG', cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty('IMG', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("IMG",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
