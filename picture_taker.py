import picamera
from time import sleep
import datetime

def getPictureName():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"


def takeAPicture():
    fullPicturePathWithName = '/home/pi/pictures/' + getPictureName() 
    print("pic name =" + fullPicturePathWithName)
    camera = picamera.PiCamera()

    camera.start_preview()
    sleep(2)
    camera.capture(fullPicturePathWithName)
    return fullPicturePathWithName

if __name__ == "__main__":
    takeAPicture()
