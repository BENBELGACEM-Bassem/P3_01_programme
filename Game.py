''' This module is responsible for managing the game,
controlling the win-loose logic and displaying the score'''

import time

import character as ch

# Create characters instances
Needle = ch.Object(0, "Needle.png")
Ether = ch.Object(1, "Ether.png")
Plastic_tube = ch.Object(2, "Plastic_tube.png")
Guardian = ch.Enemy()
MacGyver = ch.Hero()


class Game:
    ''' This class is responsible for launching the game,
    controlling the win-loose logic and displaying the score'''
    def __init__(self):
        '''Defines game properties'''
        self.score = 0

    def main(self):
        '''Main function of the game that controls launching, playing,
        winning or loosing and quitting'''
        # Draw our Characters
        ch.st.surface.blit(Ether.image, Ether.position)
        ch.st.surface.blit(Plastic_tube.image, Plastic_tube.position)
        ch.st.surface.blit(Needle.image, Needle.position)
        ch.st.surface.blit(Guardian.image, Guardian.position)
        # Draw the maze on the screen
        ch.Maze.draw_maze(ch.st.surface, "Brick.png")
        running = True
        # Need to know if McGyver already occupied an object spot so we don't
        # increase the score more than once as he enters that spot more than
        # once
        ether_already_taken = False
        plastic_tube_already_taken = False
        needle_already_taken = False

        while running:

            # Handle close event
            for event in ch.st.pygame.event.get():
                if event.type == ch.st.pygame.QUIT:
                    running = False

            # Handle pressing keys events and increasing the score as McGyver
            # picks up an object

                if event.type == ch.st.pygame.KEYDOWN:

                    if (event.key == ch.st.pygame.K_UP and
                       MacGyver.nearest_upper_spot_empty()):

                        MacGyver.moves_up()
                        if (MacGyver.picks_up(Ether) and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (MacGyver.picks_up(Plastic_tube) and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (MacGyver.picks_up(Needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_DOWN and
                       MacGyver.nearest_lower_spot_empty()):
                        MacGyver.moves_down()
                        if (MacGyver.picks_up(Ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (MacGyver.picks_up(Plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (MacGyver.picks_up(Needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_RIGHT and
                       MacGyver.nearest_right_spot_empty()):
                        MacGyver.moves_right()
                        if (MacGyver.picks_up(Ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (MacGyver.picks_up(Plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (MacGyver.picks_up(Needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_LEFT and
                       MacGyver.nearest_left_spot_empty()):
                        MacGyver.moves_left()
                        if (MacGyver.picks_up(Ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (MacGyver.picks_up(Plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (MacGyver.picks_up(Needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

            self.score_display()
            # MacGyver has to be blit under the while loop which takes care of
            # updating his position when handling events
            ch.st.surface.blit(MacGyver.image, (MacGyver.x, MacGyver.y))
            # Adding the syringe as soon as MacGyver collects the three objects
            if self.score == 3:
                ch.st.surface.blit(ch.st.pygame.image.load("seringue.png"),
                                                          (MacGyver.x,
                                                           MacGyver.y))
            ch.st.pygame.display.update()
            ch.st.clock.tick(60)

            # Check winning conditions: gathering all objects and reaching the
            # exit
            if self.score == 3 and MacGyver.finds_the_exit():
                self.win()
            # Check loosing condition: reaching the exit with at least one
            # missing object
            elif self.score < 3 and MacGyver.finds_the_exit():
                self.loose()

    def display_msg(self, text):
        '''Displays winning or loosing message at the end of the game'''
        # Define fonts
        smalltext = ch.st.pygame.font.Font('freesansbold.ttf', 20)
        largetext = ch.st.pygame.font.Font('freesansbold.ttf', 150)
        # Create an image (Surface) of the principal text, then blit this image
        # onto another Surface.
        textsurface = largetext.render(text, True, ch.st.White)
        textrectangle = textsurface.get_rect()
        textrectangle.center = (ch.st.surface_width / 2,
                                ch.st.surface_height / 2)
        ch.st.surface.blit(textsurface, textrectangle)
        # Create an image (Surface) of the standard text, then blit this image
        # onto another Surface.
        textsurface = smalltext.render(
            'Press any key to continue', True, ch.st.White)
        textrectangle = textsurface.get_rect()
        textrectangle.center = (ch.st.surface_width / 2,
                                (ch.st.surface_height / 2) +
                                2 * ch.Maze.sprite_dimension)
        ch.st.surface.blit(textsurface, textrectangle)
        # Dispaly messages on the screen
        ch.st.pygame.display.update()
        # The message holds on the screen 2 seconds even if the player press
        # rapidely any key to continue as soon as MacGyver arrives to the
        # finish position,
        time.sleep(3)

    def replay_or_quit(self):
        '''Adapt the game to the player decision once the game is over:
        quitting or playing again'''
        for event in ch.st.pygame.event.get():
            if event.type == ch.st.pygame.QUIT:
                ch.st.pygame.quit()
                quit()
            elif event.type == ch.st.pygame.KEYDOWN:
                ch.st.surface.fill(ch.st.Black)
                (MacGyver.x, MacGyver.y) = MacGyver.start_position
                self.score = 0
                self.main()

    def win(self):
        '''Displays winning message and invites the player to quit or replay'''
        self.display_msg("You win!")
        self.replay_or_quit()

    def loose(self):
        '''Displays loosing message and invites the player to quit or replay'''
        self.display_msg("You loose!")
        self.replay_or_quit()

    def score_display(self):
        '''Displays the score'''
        # Define fonts
        scoring_font = ch.st.pygame.font.Font('freesansbold.ttf', 16)
        # Create an image (Surface) of the principal text, then blit this image
        # onto another Surface.
        textsurface = scoring_font.render(
            "Score: " + str(self.score), True, ch.st.White)
        textrectangle = textsurface.get_rect()
        textrectangle.center = ch.st.surface_width - 2 * \
            ch.Maze.sprite_dimension, ch.Maze.sprite_dimension / 2
        # If the score changes, then erase the previous text
        # and blit the new one.
        # This condition will be maintained for score 1 and score 2 as they are
        # diffrent from 0
        if self.score != 0:
            textsurface.fill(ch.st.Black)
            ch.st.surface.blit(textsurface, textrectangle)
            textsurface = scoring_font.render(
                "Score: " + str(self.score), True, ch.st.White)

        ch.st.surface.blit(textsurface, textrectangle)
        ch.st.pygame.display.update()
