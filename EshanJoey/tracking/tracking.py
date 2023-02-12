import cv2
import mediapipe as mp
import time
import math
from datetime import datetime
import cvzone
from tracking.dbConnect import dbConnect
class tracking:

    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.3, #origin .5 and .8
                        min_tracking_confidence=0.6)
    mpDraw = mp.solutions.drawing_utils
    mp_face_detection = mp.solutions.face_detection
    earL, earR, eyeL, eyeR, nose, mouth = [], [], [], [], [], []




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
        t_end = time.time() + 2
        trajectory = []

        while time.time() < t_end:
            success, img = cls.cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = cls.hands.process(imgRGB)
            face_detection = cls.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
            resultsFaces = face_detection.process(imgRGB)

            # print(results.multi_hand_landmarks)
            image_height, image_width, _ = img.shape

            # faces?
            if resultsFaces.detections:
                nose = [resultsFaces.detections[0].location_data.relative_keypoints[2].x * image_width, resultsFaces.detections[0].location_data.relative_keypoints[2].y * image_height]
                flamingo_path = 'EshanJoey/tracking/madhatter-removebg-preview.png'
                flamingo = cv2.imread(flamingo_path, cv2.IMREAD_UNCHANGED)
                print(nose)
                try:
                    img = cvzone.overlayPNG(img, flamingo, [int(nose[0]), int(nose[1])])
                except:
                    print()
                    pass
            
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

                        flamingo_path = 'EshanJoey/tracking/flamingo.png'
                        flamingo = cv2.imread(flamingo_path, cv2.IMREAD_UNCHANGED)

                        try:
                            img = cvzone.overlayPNG(img, flamingo, [cx - 25, cy - 25])
                        except:
                            pass

                        hit_dic = {
                            "time": datetime.now().strftime("%H:%M:%S.%f"),
                            "triangle": (cls.perimeter(middle, pinky, thumb) * 10) **2,
                            "x": ballX * image_width,
                            "y": ballY * image_height
                        }
                        #print((cls.perimeter(middle, pinky, thumb) * 10) **2)
                        trajectory.append(hit_dic)

            cv2.putText(img, 'Move Ball with Hand!' , (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
            # cv2.resizeWindow(img, height=500, width=500)

            scale_percent = 40 # percent of original size
            im_w = int(img.shape[1] * scale_percent / 100)
            im_h = int(img.shape[0] * scale_percent / 100)
            resized = cv2.resize(img, (im_w, im_h))
            cv2.imshow("Camera Feed", resized)
            cv2.moveWindow("Camera Feed", 850, 30)
            cv2.waitKey(1)

        return image_width, trajectory

    @classmethod
    def get_duration(cls, trajectory):
        if len(trajectory) > 0:

            maxTime = trajectory[0]['time']
            minTime = trajectory[0]['time']
            maxT = trajectory[0]['triangle']
            minT = trajectory[0]['triangle']
        else:
            maxTime = 0
            minTime = 0
            maxT = 0
            minT = 0

        startX = 0
        startY = 0
        endX = 0
        endY = 0

        for d in trajectory:
            if d['triangle'] > maxT and d['x'] > 0:
                maxT = d['triangle']
                maxTime = d['time']
                endX = d['x']
                endY = d['y']
            elif d['triangle'] < minT and d['x'] > 0:
                minT = d['triangle']
                minTime = d['time']
                startX = d['x']
                startY = d['y']
            else:
                pass

        return [{
                'time': minTime,
                'x': startX,
                'y': startY,
                'tri': minT },
                {
                'time': maxTime,
                'x': endX,
                'y': endY, 
                'tri': maxT}]

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

        if (end_point['x'] > start_point['x']):  
            return -1 * (angle * 180) / math.pi
        else:
            return (angle * 180) / math.pi

    @staticmethod
    def get_time_change(p1, p2):
        p1_time_int = int(datetime.strptime(p1['time'], '%H:%M:%S.%f').microsecond)
        p2_time_int = int(datetime.strptime(p2['time'], '%H:%M:%S.%f').microsecond)
        return abs(p1_time_int - p2_time_int)


    @classmethod
    def get_power(cls, p1, p2):
        tri_ratio = abs(p1['tri'] - p2['tri'])
        return (tri_ratio / cls.get_time_change(p1, p2)) * 10000

    @classmethod
    def store_swing(cls, user, start_x, start_y, end_x, end_y, duration, angle, power):
        body = {
            "user": user,
            "start_x": start_x,
            "start_y": start_y,
            "end_x": end_x,
            "end_y": end_y,
            "duration": duration,
            "angle": angle,
            "power": power
        }
        try:
            dbConnect.setSwing(body)
            print('Successfully queried db')
        except:
            print('Error: Cannot query database')