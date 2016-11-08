from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()           #transparency 0-255
camera.annotate_text = "Hello world!"

for i in range(3):              #takes num of pictures in frame
    button.wait_for_press()
    camera.capture('/home/pi/animation/frame%03d.jpg' % i)
camera.stop_preview()

#_IP=$(hostname -I)|| true
#	if [ “$_IP” ]; then
#	  Printf “My IP address is %s\n” “$_IP”
#               fi 
#	   sleep 20
#                  sudo python /home/pi/downloads/docstation_aug.py
#	    
#               exit 0


