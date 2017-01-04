#!/usr/bin/python
def displayPathtoPrincess(n,grid):
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	for g in range(0,n):
		for j in range(0,n):
			if grid[g][j] == 'm':
				x2 = g
				y2 = j
			elif grid[g][j] == 'p':
				x1 = g
				y1 = j
			else:
				continue
            
	if x2 < x1:
	    down = x1 - x2
	    for n in range(down):
		    print('DOWN')
	if x2 > x1:
	    up = x2 - x1
	    for n in range(up):
		    print('UP')
	if y2 < y1:
	    right = y1 - y2
	    for n in range(right):
		    print('RIGHT')
	if y2 > y1:
	    left = y2 - y1
	    for n in range(left):
		    print('LEFT') 
	return 
            
#print all the moves here
m = int(input('Input for m: '))
grid = [['m','-','-'],['-','-','-'],['-','-','p']] 
for i in range(0, m): 
    grid.append(input('What to append to grid: ').strip())

displayPathtoPrincess(m,grid)
