from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime
import time


button = Button(17)
camera = PiCamera()

camera.resolution=(64,64)
camera.annotate_text = "Hello world!"
camera.rotation = 0
camera.start_preview()
while True:
        try:
                button.wait_for_press()
                camera.capture('/home/pi/usbdrv/image%s.jpg' % frame)
                frame += 1
                
        except  KeyboardInterrupt:
                camera.stop_preview()
                break
