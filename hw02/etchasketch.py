#!/usr/bin/env python3

import os
import copy
from sys import version_info
import Adafruit_BBIO.GPIO as GPIO
import time

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

def clear():
    os.system( 'clear' )
		
reset = [[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False]]
			
grid = copy.deepcopy(reset)
first = True
pos = [0,0]

up = "P9_14"
down = "P9_17"
left = "P9_15"
right = "P9_13"
resetState = "P9_11"

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)
GPIO.setup(resetState, GPIO.IN)

def mark(state):
	if state:
		return 'x'
	else:
		return ' '


def update(command):
	global first
	global pos
	global reset
	global grid
	clear()
	print('Welcome to Etch-a-Sketch!!!\n\nDirections: \nYou start in tile (0,0)\nw - up\na - left\ns - down\nd -right\nc - clear\n')
	
	#if py3:
	#	command = input("Enter Command: ")
	#else:
	#	command = raw_input("Enter Command: ")

	if command == up:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]>0:
				pos[1] = pos[1] - 1
	elif command == left:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]>0:
				pos[0] = pos[0] - 1
	elif command == down:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]<7:
				pos[1] = pos[1] + 1
	elif command == right:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]<7:
				pos[0] = pos[0] + 1
	elif command == resetState:
		grid = copy.deepcopy(reset)
		first = True
		pos = [0,0]


	if command==up or command==down or command==right or command==left:
		grid[pos[1]][pos[0]] = True

	print('   0 1 2 3 4 5 6 7')
	for i in range(8):
		print(str(i)+': '+mark(grid[i][0])+' '+mark(grid[i][1])+' '+mark(grid[i][2])+' '+mark(grid[i][3])+' '+mark(grid[i][4])+' '+mark(grid[i][5])+' '+mark(grid[i][6])+' '+mark(grid[i][7]))
update(resetState)
GPIO.add_event_detect(up, GPIO.RISING, callback=update)
GPIO.add_event_detect(down, GPIO.RISING, callback=update)
GPIO.add_event_detect(right, GPIO.RISING, callback=update)
GPIO.add_event_detect(left, GPIO.RISING, callback=update)
GPIO.add_event_detect(resetState, GPIO.RISING, callback=update)

while True:
	time.sleep(100)
