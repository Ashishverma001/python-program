# pip install opencv-contrib-python mediapipe 
import cv2 
from datetime import datetime as dt 

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
color_black = (0,0,0) # black 
color_white = ( 255,255,255) # white 

while cam.isOpened():
    status, image = cam.read()
    if status:
        # draw a box 
        cv2.rectangle(image, (5,5), (300,70), (0,255.0),2)
        # add text
        cv2.putText(image,"Live camera Feed", (10,30), font, 1, color_black,1)
        # add clock 
        timestr = dt.now().strftime("%H:%M:%S")
        cv2.putText(image,timestr, (10,70), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)
        cv2.imshow("Live camera",image)
        if cv2.waitKey(1) == 27: # 27 is the ASCII for the  Escape key
            break
cam.release()
cv2.destroyAllWindows()