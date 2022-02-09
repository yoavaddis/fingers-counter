# Made by @yyoavv
import cv2 as cv
import mediapipe as mp
import time # To check the frame rate.
import math
import hand_tracking_module as htm

# Set cam width and height to expand the app
width, height = 640, 480
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

previous_time = 0
# Create an object from hand_tracking_module.
detector = htm.handDetector(detection_con = 0.7)

tips_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    hands_img = detector.find_hands(img)
    landmarks_list, bounding_box = detector.get_position(img, draw = False)

    if len(landmarks_list) != 0:
        fingers = []

        # Thumb
        if landmarks_list[tips_ids[0]][1] > landmarks_list[tips_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers
        for id in range(1,5):
            if landmarks_list[tips_ids[id]][2] < landmarks_list[tips_ids[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        cv.putText(img, "FINGERS: " + str(fingers),(20,60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)


    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time
    cv.putText(img, "FPS: " + str(int(fps)),(20,30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
    cv.imshow("Fingers Counter", hands_img)
    cv.waitKey(1)
