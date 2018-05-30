# DMT - Underwater Drone Group B
# Author: Roy Lee
# Task: opens browser when start button in the xbox controller is pressed
import pygame
import xboxdrv
from XboxController.XboxController import XboxController
import webbrowser   # import webbrowser module
import time


# main function - opens a new tab on the open browser when start button is clicked
def browserfunction():  # function name 'browserfunction'
	webbrowser.get().open('http://192.168.4.1/html/')	# this is the static IP address of the RPi


# just to check if its working
def myCallBack(controlId,value):
	print ("Control id = {}, Value = {}".format(controlId,value))		#python 3 needs () around print

def startButtonCallBack(value):
	print ("Active")
	browserfunction()


# defining xboxCont
try:
	xboxCont=XboxController( 		#class
		controllerCallBack=myCallBack,
		joystickNo=0,
		deadzone=0.1,
		scale=1,
		invertYAxis = False)

	# starts gathering input from the controller
	xboxCont.start()

	xboxCont.setupControlCallback(
		xboxCont.XboxControls.START,
		startButtonCallBack)

	while True:		# keeps it looking for input indefinitely
		print (" still alive")	# check if code works
		time.sleep(10)

	xboxCont.stop()
except pygame.error as e:
	print("An exception was thrown. Is the xbox controller connected?")
	print(e)
	input("Press enter to quit. ")