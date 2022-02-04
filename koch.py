import turtle

def Koch(iterations):
	length = 200
	Koch = 'FRFRF'
	
	turtle.penup()
	turtle.speed(0)
	turtle.setpos(-length*3/2, length*3/4)

	for _ in range (iterations):
		Koch = Koch.replace('F', 'FLFRFLF')

	turtle.pendown()

	turtle.color('black','skyblue')
	turtle.begin_fill()

	for move in Koch:
		if move == 'F':
			turtle.forward(length/(3**(iterations-1)))
		elif move == 'L':
			turtle.left(60)
		elif move == 'R':
			turtle.right(120)

	turtle.end_fill()
	turtle.mainloop()