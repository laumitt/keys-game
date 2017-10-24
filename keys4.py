setup
- where are the walls
- where are the crystals
- how do you know where you can move
- how do you move
- how do you hold things

steps
- where do you start
- loop
	- where can you go
	- where do you want to go
	- do you need a key
	- do you have that key
	- move
	- did you find something
- if you have all the crystals and are you at the end
	- congrats you won

# to find starting position
sy = -1 # not set yet
sx = -1 # not set yet
maze = open('Maze.txt', 'r').read().split('\n') # open the maze file, read it, and split it at each new line
for y, line in enumerate(maze): # for each line and each index of each line in maze
	if line.find('s') != -1: # if s is on that line, line.find will return its index
		sy = y # sy is the starting y coordinate now set to the line number of s
		sx = line.find('s') # sx is the starting x coordinate now set to the index of s
		break # if s was found, stop looking
class Walls:
	def checkWalls:
		for y, line in enumerate(maze):
			if line.find('+') != -1 and line.find(' ') != -1:
				if line.find('c') != -1:
					# not sure where this is going