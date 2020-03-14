
from Character import *
from random import sample
import time

class Game:
	def __init__(self):
		self.score=0

	def main(self):
		#Draw our Characters
		surface.blit(Ether.image, Ether.position)
		surface.blit(Plastic_tube.image, Plastic_tube.position)
		surface.blit(Needle.image, Needle.position)
		surface.blit(Guardian.image, Guardian.position)
		#Draw the maze on the screen 
		Maze.draw_maze(surface,"Brick.png")
		running = True
		#Need to know if McGyver already occupied an object spot so we don't increase the score more than once as he enters that spot more than once
		Ether_already_taken=False
		Plastic_tube_already_taken=False
		Needle_already_taken=False

		while running:

			#Handle close event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running=False

			#Handle pressing keys events and increasing the score as McGyver picks up an object 

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_UP and MacGyver.nearest_upper_spot_empty():

						MacGyver.move_up()
						if (MacGyver.picks_up(Ether) and Ether_already_taken==False):
							self.score+=1
							Ether_already_taken=True
						if (MacGyver.picks_up(Plastic_tube) and Plastic_tube_already_taken==False):
							self.score+=1
							Plastic_tube_already_taken=True
						if (MacGyver.picks_up(Needle) and Needle_already_taken==False):
							self.score+=1
							Needle_already_taken=True


					if event.key == pygame.K_DOWN and MacGyver.nearest_lower_spot_empty():
						MacGyver.move_down()
						if (MacGyver.picks_up(Ether) and Ether_already_taken==False):
							self.score+=1
							Ether_already_taken=True
						if (MacGyver.picks_up(Plastic_tube) and Plastic_tube_already_taken==False):
							self.score+=1
							Plastic_tube_already_taken=True
						if (MacGyver.picks_up(Needle) and Needle_already_taken==False):
							self.score+=1
							Needle_already_taken=True


					if event.key == pygame.K_RIGHT and MacGyver.nearest_right_spot_empty():
						MacGyver.move_right()
						if (MacGyver.picks_up(Ether) and Ether_already_taken==False):
							self.score+=1
							Ether_already_taken=True
						if (MacGyver.picks_up(Plastic_tube) and Plastic_tube_already_taken==False):
							self.score+=1
							Plastic_tube_already_taken=True
						if (MacGyver.picks_up(Needle) and Needle_already_taken==False):
							self.score+=1
							Needle_already_taken=True


					if event.key == pygame.K_LEFT and MacGyver.nearest_left_spot_empty():
						MacGyver.move_left()
						if (MacGyver.picks_up(Ether) and Ether_already_taken==False):
							self.score+=1
							Ether_already_taken=True
						if (MacGyver.picks_up(Plastic_tube) and Plastic_tube_already_taken==False):
							self.score+=1
							Plastic_tube_already_taken=True
						if (MacGyver.picks_up(Needle) and Needle_already_taken==False):
							self.score+=1
							Needle_already_taken=True


			self.score_display()
			#MacGyver has to be blit under the while loop which takes care of updating his position when handling events
			surface.blit(MacGyver.image, (MacGyver.x, MacGyver.y))
			#Adding the syringe as soon as MacGyver collects the three objects
			if self.score==3:
				surface.blit(pygame.image.load("seringue.png"),(MacGyver.x, MacGyver.y))
			pygame.display.update()
			clock.tick(60)

			#Check winning conditions: gathering all objects and reaching the exit
			if self.score==3 and MacGyver.finds_the_exit():
					self.win()
			#Check loosing condition: reaching the exit with at least one missing object
			elif self.score<3 and MacGyver.finds_the_exit():
					self.loose()


	def display_msg(self,text):

		#Define fonts
		smalltext=pygame.font.Font('freesansbold.ttf', 20)
		largetext=pygame.font.Font('freesansbold.ttf', 150)
		#Create an image (Surface) of the principal text, then blit this image onto another Surface.
		textsurface=largetext.render(text, True, White)
		textrectangle=textsurface.get_rect()
		textrectangle.center=surface_width/2,surface_height/2
		surface.blit(textsurface,textrectangle)
		#Create an image (Surface) of the standard text, then blit this image onto another Surface.
		textsurface=smalltext.render('Press any key to continue', True, White)
		textrectangle=textsurface.get_rect()
		textrectangle.center=surface_width/2,(surface_height/2)+100
		surface.blit(textsurface,textrectangle)
		#Dispaly messages on the screen 
		pygame.display.update()


	def replay_or_quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				surface.fill(black)
				(MacGyver.x, MacGyver.y)=MacGyver.start_position
				self.score=0
				self.main()

	def win(self):
		self.display_msg("You win!")
		self.replay_or_quit()

	def loose(self):
		self.display_msg("You loose!")
		self.replay_or_quit()

	def score_display(self):
		#Define fonts
		scoring_font=pygame.font.Font('freesansbold.ttf', 16)
		#Create an image (Surface) of the principal text, then blit this image onto another Surface.
		textsurface=scoring_font.render("Score: " + str(self.score), True, White)
		textrectangle=textsurface.get_rect()
		textrectangle.center=surface_width-2*Maze.sprite_dimension,Maze.sprite_dimension/2
		#If the score changes, then erase the previous text and blit the new one.
		#This condition will be maintained for score 1 and score 2 as they are diffrent from 0
		if self.score!=0:
			textsurface.fill(black)
			surface.blit(textsurface,textrectangle)
			textsurface=scoring_font.render("Score: " + str(self.score), True, White)			

		surface.blit(textsurface,textrectangle)
		pygame.display.update()




#Create a game instance
Escape=Game()
















