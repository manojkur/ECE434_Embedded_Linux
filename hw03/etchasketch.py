#!/usr/bin/env python3

import os
import copy
from sys import version_info
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import time
import smbus
from functools import reduce


bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

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

resetState = "P9_11"

GPIO.setup(resetState, GPIO.IN)

verticalEncoder = RotaryEncoder(eQEP1)
horizontalEncoder = RotaryEncoder(eQEP2)
verticalEncoder.setAbsolute()
horizontalEncoder.setAbsolute()
verticalEncoder.enable()
horizontalEncoder.enable()

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

output = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]



def mark():
	global grid
	global output
	for row in range(len(grid)):
		output[row*2] = reduce(lambda a, b: (a<<1) + int(b), grid[row])

while True:
	clear()
	#print('Welcome to Etch-a-Sketch!!!\n\nDirections: \nYou start in tile (0,0)\nw - up\na - left\ns - down\nd -right\nc - clear\n')


	if verticalEncoder.position < 0:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]>0:
				pos[1] = pos[1] - 1
	elif horizontalEncoder.position < 0:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]>0:
				pos[0] = pos[0] - 1
	elif verticalEncoder.position > 0:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]<7:
				pos[1] = pos[1] + 1
	elif horizontalEncoder.position > 0:
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]<7:
				pos[0] = pos[0] + 1
	elif GPIO.input(resetState):
		grid = copy.deepcopy(reset)
		output =  [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
			0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		first = True
		pos = [0,0]


	if horizontalEncoder.position!=0 or verticalEncoder.position!=0:
		grid[pos[0]][pos[1]] = True

	horizontalEncoder.position = 0
	verticalEncoder.position = 0
	mark()
	bus.write_i2c_block_data(matrix, 0, output)
	time.sleep(0.2)
