#!/usr/bin/env python
# this file is run using this command: "sudo python camera.py"
# python must be installed, and you must call the command while
# you are in the same folder as the file
from time import sleep
import os
import RPi.GPIO as GPIO
import subprocess
import datetime
import pygame
# set up the pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN)
# setup variables
count = 0 
up = False
down = False
command = ""
filename = ""
index = 0
camera_pause = "500"
print ("Raspberry Pi Camera with Buttons")

def takepic(imageName):
    print("click")
    command = "sudo raspistill -o " + imageName + " -q 100 -t " + camera_pause
    print(command)
    os.system(command)
while(True):
    for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
    if(up==True):
            if(GPIO.input(13)==False):

                        print ("BUTTON DOWN PRESSED")

            now = datetime.datetime.now()
                       
            timeString = now.strftime("%Y-%m-%d_%H:%M:%S")
                        
            print("request received" + timeString)

            filename = "photo-" + timeString + ".jpg"
                        
            takepic(filename)
    
    up = GPIO.input(13)
    
    count = count +1
    
    sleep(.1)
    
# this is never hit, but should be here to indicate if you plan on leaving the main loop


print ("done")
