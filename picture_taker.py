import picamera
from time import sleep



def takeAPicture():
    camera = picamera.PiCamera()

    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
