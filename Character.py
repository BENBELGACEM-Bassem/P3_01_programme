
from random import sample
import time
from Structure import *


class Hero:

	def __init__(self):

		self.width=32
		self.height=40
		#Putting MacGyver at the center of the entrance spot
		self.distance_to_horizontal_edge= (Maze.sprite_dimension-self.width)/2
		self.distance_to_vertical_edge = (Maze.sprite_dimension-self.height)/2
		self.x= Maze.entrance[0][0]+self.distance_to_horizontal_edge
		self.y=Maze.entrance[0][1]+self.distance_to_vertical_edge
		#MacGyver move by a step of 50
		self.speed=Maze.sprite_dimension
		self.image=pygame.image.load("MacGyver.png")
		self.start_position=(self.x,self.y)
	
	#The following functions define four possible mouvement.
	#Within each mouvement function, draw a black rectangle in same position of our hero image before moving it, so the previous state is hidden
	def move_up(self):
		pygame.draw.rect(surface,(0,0,0),(self.x, self.y, self.width, self.height))
		self.y-=self.speed	
	def move_down(self):
		pygame.draw.rect(surface,(0,0,0),(self.x, self.y, self.width, self.height))
		self.y+=self.speed
	def move_right(self):
		pygame.draw.rect(surface,(0,0,0),(self.x, self.y, self.width, self.height))
		self.x+=self.speed
	def move_left(self):
		pygame.draw.rect(surface,(0,0,0),(self.x, self.y, self.width, self.height))
		self.x-=self.speed		

	def nearest_left_spot_empty(self):
	# 	#Return True if the nearest left (x,y) couple is within passage_positions list, containing empty spots of the Maze
		return ((self.x-(self.distance_to_horizontal_edge + Maze.sprite_dimension)), (self.y-self.distance_to_vertical_edge)) in Maze.passage_positions 
	def nearest_right_spot_empty(self):
	# 	#Return True if the nearest right (x,y) couple is within passage_positions list, containing empty spots of the Maze
		return ((self.x+Maze.sprite_dimension-self.distance_to_horizontal_edge), (self.y-self.distance_to_vertical_edge)) in Maze.passage_positions
	def nearest_upper_spot_empty(self):
	# 	#Return True if the nearest upper (x,y) couple is within passage_positions list, containing empty spots of the Maze
		return ((self.x-self.distance_to_horizontal_edge), self.y-(self.distance_to_vertical_edge+ Maze.sprite_dimension)) in Maze.passage_positions 
	def nearest_lower_spot_empty(self):
	# 	#Return True if the nearest lower (x,y) couple is within passage_positions list, containing empty spots of the Maze
		return ((self.x-self.distance_to_horizontal_edge), self.y+Maze.sprite_dimension-self.distance_to_vertical_edge) in Maze.passage_positions

	#check if MacGyver reach the position of an empty cell where there is an object(which is the name of the instance not the class)
	def picks_up(self, object):
		return (self.x-self.distance_to_horizontal_edge, self.y-self.distance_to_vertical_edge)== (object.x-object.distance_to_horizontal_edge, object.y-object.distance_to_vertical_edge)
	#Check if MacGyver reach the exit of the Maze
	def finds_the_exit(self):
		 return [(self.x-self.distance_to_horizontal_edge, self.y-self.distance_to_vertical_edge)]== Maze.exit		 	

class Enemy:

	def __init__(self):
		self.width=32
		self.height=36
		self.x= Maze.enemy_location[0][0] +(Maze.sprite_dimension-self.width)/2
		self.y=Maze.enemy_location[0][1] +(Maze.sprite_dimension-self.height)/2
		self.position=(self.x,self.y)
		self.image=pygame.image.load("Gardien.png")


class Object:
	#Three objects to create
	Number=3
	#Using sample function to insure getting three different couples of coordinates (x,y) from the object locations list
	#Make this property a class property, so it is not recreated with each instance to avoid a possible case where two or more objects are in the same location
	random_positions=sample(Maze.objects_locations,Number)
	def __init__(self, index, image):
		#Limit the object index to 0,1 or 2 as we have only 3 objects to gather
		if index not in range(Object.Number):
			raise ValueError (f"Please enter a value in {list(range(Object.Number))} ")
		self.index=index
		self.image=pygame.image.load(image)
		self.width=30
		self.height=30
		self.distance_to_horizontal_edge= (Maze.sprite_dimension-self.width)/2
		self.distance_to_vertical_edge = (Maze.sprite_dimension-self.height)/2
		#Choose randomly, three (x,y) couples from empty spot of the Maze. Then,depending on the object index, assign an (x,y) from this list to this object
		#Center the object in the empty spot
		self.x= Object.random_positions[self.index][0]+self.distance_to_horizontal_edge
		self.y= Object.random_positions[self.index][1]+self.distance_to_vertical_edge
		self.position=(self.x, self.y)

#Create character instances as well as the Maze instance
Needle=Object(0,"Needle.png")
Ether=Object(1,"Ether.png")
Plastic_tube=Object(2,"Plastic_tube.png")
Guardian=Enemy()
MacGyver=Hero()

































