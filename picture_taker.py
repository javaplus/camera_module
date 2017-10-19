import picamera
from time import sleep
import datetime

def getPictureName():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"


def takeAPicture():
    fullPicturePathWithName = '/home/pi/pictures/' + getPictureName() 
    print("pic name =" + fullPicturePathWithName)
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)

    camera.start_preview()
    sleep(2)
    camera.capture(fullPicturePathWithName)
    camera.close()
    print("Captured pic")
    return fullPicturePathWithName

if __name__ == "__main__":
    takeAPicture()
