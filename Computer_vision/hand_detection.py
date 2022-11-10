import cv2 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cam = cv2.videoCapture(0)
with mp-mp_hands.Hands(model_complaxity=0,
    min_detection_confidence =.5,
    min_tracking_confidence =.5) as hands:

    while cam.isOpened():
        status, image = cam.read()
        if not status:
            break
        image.flages.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS, 
                    mp_drawing_styles.get_default_hand_landmarks_style(), 
                    mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('Mediapipe example', image)
        if cv2.waitKey(5) == 27:
            break
cam.release()
cv2.destroyAllWindows()