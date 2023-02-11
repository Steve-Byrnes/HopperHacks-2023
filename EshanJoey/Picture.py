import requests
import cv2
from PIL import Image
from io import BytesIO
import time



def getFrame():
    timeNow = str(time.time())
    camera = requests.get("https://webcams.nyctmc.org/api/cameras/c34ca47e-e375-4b9f-a8d7-f9737566b783/image?t=" + timeNow, verify=False)

    return Image.open(BytesIO(camera.content))
    #print(type(img))
    
    

while True:
       
    # Get a numpy array to display from the simulation
    npimage=getFrame()

    cv2.imshow('image',npimage)
    cv2.waitKey(1)