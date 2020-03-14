import pygame

pygame.init()

#Pygame boiler plate, to initialize the module, define our play screen size and name as well as time tracking
surface_width= 770
surface_height=770
surface=pygame.display.set_mode((surface_width,surface_height))
pygame.display.set_caption("Escape_game")
clock=pygame.time.Clock()

#The class structure contains needed function and properties to define the maze
class Structure:

	def __init__(self):
		self.sprite_dimension=45
		self.map =[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
				  [2,1,1,1,"E",1,1,1,1,1,1,1,1,1,1,1,2],
                   [2,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2],
                   [2,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,2],
                   [2,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,2],
                   [2,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,2],
                   [2,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,2],
                   [2,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,2],
                   [2,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,2],
                   [2,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,2],
                   [2,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,2],
                   [2,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,2],
                   [2,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,2],
                   [2,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,2],
                   [2,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,2],
                  [2,1,1,1,1,1,1,1,1,1,1,1,1,1,"S",1,2],
                  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,"G",2,2]]

		self.entrance=[(column*self.sprite_dimension,row*self.sprite_dimension) for row in range(len(self.map)) for column in range(len(self.map[row])) if self.map[row][column]=="E"]
		self.exit=[(column*self.sprite_dimension,row*self.sprite_dimension) for row in range(len(self.map)) for column in range(len(self.map[row])) if self.map[row][column]=="S"]
	
   #Once called, this functopn will draw the Maze
	def draw_maze(self,surface,sprite):
		image=pygame.image.load(sprite)
		for row in range(len(self.map)):
			for column in range(len(self.map[row])):
				if self.map[row][column]==1:
					surface.blit(image,(column*self.sprite_dimension,row*self.sprite_dimension))

	#This property define the empty positions inside the Maze where it is probable to find an object
	@property
	def objects_locations(self):
		objects_locations=[]
		for row in range(len(self.map)):
			for column in range(len(self.map[row])):
				if self.map[row][column]==0:
					objects_locations.append((column*self.sprite_dimension,row*self.sprite_dimension))
		return objects_locations	

	#This property define the empty positions inside the Maze where MacGyver could move
	@property
	def passage_positions(self):
		passage_positions=[]
		for row in range(len(self.map)):
			for column in range(len(self.map[row])):
				if self.map[row][column]==0 or self.map[row][column]=="E" or self.map[row][column]=="S":
					passage_positions.append((column*self.sprite_dimension,row*self.sprite_dimension))
		return passage_positions	

	#This property define the empty positions inside the Maze where the guardian could stand
	@property
	def enemy_location(self):
		enemy_location=[]
		for row in range(len(self.map)):
			for column in range(len(self.map[row])):
				if self.map[row][column]=="G":
					enemy_location.append((column*self.sprite_dimension,row*self.sprite_dimension))
		return enemy_location
	

#Create Maze instance
Maze=Structure()
	
	