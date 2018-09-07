#!/usr/bin/env python3

def mark(state):
	if state:
		return ' '
	else:
		return 'x'

pos = [0,0]

grid = [[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False]]

print('   0 1 2 3 4 5 6 7')

for i in range(8):
	print(i+': '+mark(grid[i,0])+' '+mark(grid[i,1])+' '+mark(grid[i,2])+' '+mark(grid[i,3])+' '
		+mark(grid[i,4])+' '+mark(grid[i,5])+' '+mark(grid[i,6])+' '+mark(grid[i,7]))
