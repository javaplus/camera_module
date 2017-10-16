import picamera
from time import sleep
import datetime

def getPictureName():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"


def takeAPicture():
    camera = picamera.PiCamera()

    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    fullPicturePathWithName = '/home/pi/pictures/' + getPictureName() 
    camera.capture(fullPicturePathWithName)
    camera.stop_preview()
    return fullPicturePathWithName

if __name__ == "__main__":
    takeAPicture()
