import cv2
import mediapipe as mp
import time
import math
from datetime import datetime

class tracking:

    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils

    # pTime = 0
    # cTime = 0

    @staticmethod
    def dist(point1, point2):
        if point1 is None or point1 is None:
            pass
        if not isinstance(point1, list) or not isinstance(point2, list):
            pass
        dX = point1[0] - point2[0]
        dY = point1[1] - point2[1]
        return math.sqrt(dX**2 + dY**2)

    @classmethod
    def perimeter(cls, point1, point2, point3):
        if point1 is None or point2 is None or point3 is None:
            pass
        if not isinstance(point1, list) or not isinstance(point2, list) or not isinstance(point3, list):
            pass
        return cls.dist(point1, point2) + cls.dist(point2, point3) + cls.dist(point1,point3)

    @classmethod
    def trackHit(cls):

        t_end = time.time() + 5
        trajectory = []

        while time.time() < t_end:
            success, img = cls.cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = cls.hands.process(imgRGB)
            # print(results.multi_hand_landmarks)

            # num of hands
            if results.multi_hand_landmarks:
                # num of points for hand
                for handLms in results.multi_hand_landmarks:

                    middleX = handLms.landmark[cls.mpHands.HandLandmark.MIDDLE_FINGER_TIP].x
                    middleY = handLms.landmark[cls.mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
                    middle = [middleX, middleY]

                    pinkyX = handLms.landmark[cls.mpHands.HandLandmark.PINKY_TIP].x
                    pinkyY = handLms.landmark[cls.mpHands.HandLandmark.PINKY_TIP].y
                    pinky = [pinkyX, pinkyY]

                    thumbX = handLms.landmark[cls.mpHands.HandLandmark.THUMB_TIP].x
                    thumbY = handLms.landmark[cls.mpHands.HandLandmark.THUMB_TIP].y
                    thumb = [thumbX, thumbY]

                    ballX = handLms.landmark[cls.mpHands.HandLandmark.MIDDLE_FINGER_MCP].x
                    ballY = handLms.landmark[cls.mpHands.HandLandmark.MIDDLE_FINGER_MCP].y

                    hit_dic = {
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "triangle": (cls.perimeter(middle, pinky, thumb) * 10) **2,
                        "x": ballX,
                        "y": ballY
                    }

                    trajectory.append(hit_dic)

                    # for id, lm in enumerate(handLms.landmark):
                    #     h, w, c = img.shape
                    #     cx, cy = int(lm.x *w), int(lm.y*h)
                    #     cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


            # cTime = time.time()
            # fps = 1/(cTime-pTime)
            # pTime = cTime

            # # cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

        return trajectory

        