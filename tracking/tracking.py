import cv2
import mediapipe as mp
import time
import math
from datetime import datetime
import cvzone

class tracking:

    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils

    # pTime = 0
    # cTime = 0

    starting_screen_bound = 200

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

        t_end = time.time() + 60
        trajectory = []
        countdown = int(datetime.now().strftime("%S"))

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

                    # hit_dic = {
                    #     "time": datetime.now().strftime("%H:%M:%S"),
                    #     "triangle": (cls.perimeter(middle, pinky, thumb) * 10) **2,
                    #     "x": ballX,
                    #     "y": ballY
                    # }

                    # trajectory.append(hit_dic)

                    point_list = [handLms.landmark[cls.mpHands.HandLandmark.MIDDLE_FINGER_MCP]]

                    flag = [655, 564]

                    for id, lm in enumerate(point_list):
                        h, w, c = img.shape
                        cx, cy = int(lm.x *w), int(lm.y*h)
                        point = [cx, cy]

                        # if cy > cls.starting_screen_bound:
                        #     circle_image = cv2.circle(img, (cx,cy), 60, (30,215,96), cv2.FILLED)
                        # else:
                        #     circle_image = cv2.circle(img, (cx,cy), 60, (0,0,0), cv2.FILLED)

                        flamingo_path = 'flamingo.png'
                        flamingo = cv2.imread(flamingo_path, cv2.IMREAD_UNCHANGED)

                        try:
                            img = cvzone.overlayPNG(img, flamingo, [cx - 25, cy - 25])
                        except:
                            pass

                        hit_dic = {
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "triangle": (cls.perimeter(middle, pinky, thumb) * 10) **2,
                            "x": cx,
                            "y": cy
                        }

                        trajectory.append(hit_dic)

                        
            # cTime = time.time()
            # fps = 1/(cTime-pTime)
            # pTime = cTime
            if (int(datetime.now().strftime("%S")) != countdown):
                countdown = int(datetime.now().strftime("%S"))

            cv2.putText(img, 'Hello Eshan' , (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

        return trajectory

    @classmethod
    def get_duration(cls, trajectory):
        maxTime = trajectory[0]['time']
        minTime = trajectory[0]['time']
        maxT = trajectory[0]['triangle']
        minT = trajectory[0]['triangle']

        startX = 0
        startY = 0
        endX = 0
        endY = 0

        for d in trajectory:
            if d['triangle'] > maxT:
                maxT = d['triangle']
                maxTime = d['time']
                endX = d['x']
                endY = d['y']
            elif d['triangle'] < minT:
                minT = d['triangle']
                minTime = d['time']
                startX = d['x']
                startY = d['y']
            else:
                pass

        return [{
                'time': minTime,
                'x': startX,
                'y': startY}, 
                {
                'time': maxTime,
                'x': endX,
                'y': endY}]

    @classmethod
    def get_angle(cls, start_point, end_point):

        # distance from start-to-end
        starting = [start_point['x'], start_point['y']]
        # starting = [.46, .87]
        ending = [end_point['x'], end_point['y']]
        distPath = cls.dist(starting, ending)

        # distance from start-to-temp
        temp = [start_point['x'], end_point['y']]
        distTemp = cls.dist(starting, temp)

        angle = math.acos(distTemp / distPath)   
        return (angle * 180) / math.pi

        