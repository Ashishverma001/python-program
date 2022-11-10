import cv2 

cam = cv2.VideoCapture(0)

while cam.isOpened():
    status, image = cam.read()
    if status:
        cv2.imshow("Live camera", image)
        if cv2.waitKey(1) == 27: # 27 is the ASCII for the  Escape key
            break
cam.release()
cv2.destroyAllWindows()