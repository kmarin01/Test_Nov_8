from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 0
camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/usbdrv/image2.jpg')
camera.stop_preview()
