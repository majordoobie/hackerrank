import random
x = int(input('Input for x: '))
y = int(input('Inpur for y: '))
mark = '-'

#initialize the matrix
matrix = [[mark for j in range(0,x)]for n in range(0,y)]
for row in matrix:
	print(' '.join(row))
	
	
#randomly place p and m
ranx_m = random.randrange(0,x)
rany_m = random.randrange(0,y)
ranx_p = random.randrange(0,x)
rany_p = random.randrange(0,y)

matrix[ranx_m][rany_m] = 'm'
matrix[ranx_p][rany_p] = 'p'
print('\n\n')

for row in matrix:
	print(' '.join(row))
print('\n\n')


#finding the location of p and m
for n in range(0,x):
	for j in range(0,y):
		if matrix[n][j] == 'm':
			print("The location of 'm' is [",n,"][",j,"]")
			x2 = n
			y2 = j
		elif matrix[n][j] == 'p':
			print("The location of 'p' is [",n,"][",j,"]")
			x1 = n
			y1 = j
		else:
			continue 
			
			
			
#printing the coordinates 
print('\n\n')
print("'m' coordinates are (", x2 ,",", y2 ,")")
print("'p' coordinates are (", x1 ,",", y1 ,")")
print('\n\n')

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



	
