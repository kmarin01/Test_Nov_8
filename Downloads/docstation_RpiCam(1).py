Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
#!/usr/bin/python3.4
#this code only saves photos locally. demo purposes only
#this script is for using the rpi camera module
from picamera import PiCamera
import sys

import os

import pygame

import datetime
import time

import RPi.GPIO as GPIO

import subprocess
from subprocess import call

#make sure pins are labeled properly: pin 16 for pic taking and 13 for program exit
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#open pygames environment and determine camera source/resolution
pygame.init()

pygame.camera.init()

#create fullscreen display

screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

#find, open and start cam ..this part might need editing. not sure if camera list is needed

camera = PiCamera()

camera.resolution = (800, 480)

camera.start_preview()

#for naming the images
paths = []
usbnames = []
comp = datetime.datetime.now().date()
hi = str(datetime.datetime.now().date())
hi = hi.replace(".", "_")
hi = hi.replace(" ", "_")
hi = hi.replace(":", "_")
#paths.append("/home/pi/usbdrv/%s" %hi)

font = pygame.font.Font(None, 25)

i = 0

def record(runtime):
        global path

        global hi
        
        global i

        start_time = time.time()

        last_frame = 0

        current_frame = 0

        fps = 0

        if True :

                        #grab image...

                        time_left = int(runtime - (time.time() - start_time))
                        #changed from "webcam" to "camera" as we relabeled it above
                        imagen = camera.get_image()

                        imagen = pygame.transform.scale(imagen, (800, 480))



                        last_frame = current_frame
                        current_frame = time.time()
                        ti =str(datetime.datetime.now().time())
                        ti = ti.replace(".", "_")
                        ti = ti.replace(" ", "_")
                        ti = ti.replace(":", "")
                        ti = ti[0:4]

                        fps = 1/(current_frame - last_frame)



                        #display_time = "FPS: %d   Time left: %d" %(fps, time_left)

                        #text = font.render(display_time, True, (255,255,255))



                        screen.blit(imagen, (0,0))



                        #usbname = "/home/pi/usbdrv/Photos/%(1)s_%(2)s_%(3)s.jpg" % {"1": hi,"2": ti,"3" : i}
                        newphoto = "/home/pi/DocPhotos/%(1)s_%(2)s_%(3)s.jpg" % {"1": hi,"2": ti,"3" : i}


                        #pygame.image.save(imagen, usbname)
                        pygame.image.save(imagen, newphoto)
                        


                        #usbnames.append(usbname)
                        newphotos.append(newphoto)
                        

                        pygame.display.update()

                        i = i+1

        #return usbnames
        return newphotos



while True:



        runtime = 0

        start_time = time.time()

        last_frame = 0

        current_frame = 0

        fps = 0

        #usbnames = []
        newphotos = []

        #grab image...

        time_left = int(runtime - (time.time() - start_time))

        imagen = camera.get_image()

        imagen = pygame.transform.scale(imagen, (800, 480))



        last_frame = current_frame

        current_frame = time.time()

        fps = 1/(current_frame - last_frame)

        screen.blit(imagen, (0,0))

        display_msg = "Press the button to take pictures!"

        text2 = font.render(display_msg, True, (0,0,255))

        #have screenfill with current image if possible

        #screen.fill((0,0,0))

        screen.blit(text2, (220, 220))

        pygame.display.update()


       #big pushbutton to take picture 
        input_state = GPIO.input(16)

        if input_state == False:


                #usbnames = record(1)
		newphotos = record(1)

                delete_option = "Press button again to delete?"

                text4 = font.render(delete_option, True, (255,255,255))


                screen.blit(text4, (220, 220))

                pygame.display.update()
                
                cur_time = time.time()

                time.sleep(0.5)


                while time.time() - cur_time < 4 or input_state2 == False :

                        input_state2 = GPIO.input(16)

                        if input_state2 == False:
                                
                                #for usbname in usbnames:
				for newphoto in newphotos:
                                        
                                         #os.remove(usbname)
                                         os.remove(newphoto)
                                         
                                time.sleep(0.5)
                                
                                break
        #exit documentation program and take to homescreen

        input_state3 = GPIO.input(13)

        
        if input_state3 == False:
                
                        screen.fill((0,0,0))

                        thank_you = "Thanks for your pictures! Don't forget to upload new photos from thumb drive!"

                        text3 = font.render(thank_you, True, (255,255,255))
			text3rect = text3.get_rect()
			text3rect.centerx = screen.get_rect().centerx
			text3rect.centery = screen.get_rect().centery
                        screen.blit(text3, text3rect)

                        pygame.display.update()

                        time.sleep(4)
                        #change from "webcam" to "camera"
                        camera.stop()

                        pygame.quit()

                        sys.exit()
