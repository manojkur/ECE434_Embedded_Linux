#!/usr/bin/env python3

import os
import copy
from sys import version_info

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

def mark(state):
	if state:
		return 'x'
	else:
		return ' '

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

while True:

	clear()
	print('Welcome to Etch-a-Sketch!!!\n\nDirections: \nYou start in tile (0,0)\nw - up\na - left\ns - down\nd -right\nc - clear\n')

	print('   0 1 2 3 4 5 6 7')
	for i in range(8):
		print(str(i)+': '+mark(grid[i][0])+' '+mark(grid[i][1])+' '+mark(grid[i][2])+' '+mark(grid[i][3])+' '+mark(grid[i][4])+' '+mark(grid[i][5])+' '+mark(grid[i][6])+' '+mark(grid[i][7]))
	
	if py3:
		command = input("Enter Command: ")
	else:
		command = raw_input("Enter Command: ")

	if command == 'w':
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]>0:
				pos[1] = pos[1] - 1
	elif command == 'a':
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]>0:
				pos[0] = pos[0] - 1
	elif command == 's':
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[1]<7:
				pos[1] = pos[1] + 1
	elif command == 'd':
		if first:
			first = False
			grid[0][0] = True
		else:
			if pos[0]<7:
				pos[0] = pos[0] + 1
	elif command == 'c':
		grid = copy.deepcopy(reset)
		first = True
		pos = [0,0]


	if command=='w' or command=='a' or command=='s' or command=='d':
		grid[pos[1]][pos[0]] = True
