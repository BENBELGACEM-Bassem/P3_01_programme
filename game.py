# This module is responsible for managing the game,
# controlling the win-loose logic and displaying the score

import time

import character as ch

# Create characters instances
needle = ch.Object(0, "Needle.png")
ether = ch.Object(1, "Ether.png")
plastic_tube = ch.Object(2, "Plastic_tube.png")
guardian = ch.Enemy()
macgyver = ch.Hero()


class Game:
    """This class is responsible for launching the game,
    controlling the win-loose logic and displaying the score"""
    def __init__(self):
        """Defines game properties"""
        self.score = 0

    def main(self):
        """Main function of the game that controls launching, playing,
        winning or loosing and quitting"""
        # Draw our Characters
        ch.st.SURFACE.blit(ether.image, ether.position)
        ch.st.SURFACE.blit(plastic_tube.image, plastic_tube.position)
        ch.st.SURFACE.blit(needle.image, needle.position)
        ch.st.SURFACE.blit(guardian.image, guardian.position)
        # Draw the maze on the screen
        ch.maze.draw_maze(ch.st.SURFACE, "Brick.png")
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
                       macgyver.nearest_upper_spot_empty()):

                        macgyver.moves_up()
                        if (macgyver.picks_up(ether) and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (macgyver.picks_up(plastic_tube) and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (macgyver.picks_up(needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_DOWN and
                       macgyver.nearest_lower_spot_empty()):
                        macgyver.moves_down()
                        if (macgyver.picks_up(ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (macgyver.picks_up(plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (macgyver.picks_up(needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_RIGHT and
                       macgyver.nearest_right_spot_empty()):
                        macgyver.moves_right()
                        if (macgyver.picks_up(ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (macgyver.picks_up(plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (macgyver.picks_up(needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

                    if (event.key == ch.st.pygame.K_LEFT and
                       macgyver.nearest_left_spot_empty()):
                        macgyver.moves_left()
                        if (macgyver.picks_up(ether)and not
                           ether_already_taken):
                            self.score += 1
                            ether_already_taken = True
                        if (macgyver.picks_up(plastic_tube)and not
                           plastic_tube_already_taken):
                            self.score += 1
                            plastic_tube_already_taken = True
                        if (macgyver.picks_up(needle)and not
                           needle_already_taken):
                            self.score += 1
                            needle_already_taken = True

            self.score_display()
            # macgyver has to be blit under the while loop which takes care of
            # updating his position when handling events
            ch.st.SURFACE.blit(macgyver.image, (macgyver.x, macgyver.y))
            # Adding the syringe as soon as macgyver collects the three objects
            if self.score == 3:
                ch.st.SURFACE.blit(ch.st.pygame.image.load("seringue.png"),
                                                          (macgyver.x,
                                                           macgyver.y))
            ch.st.pygame.display.update()
            ch.st.CLOCK.tick(60)

            # Check winning conditions: gathering all objects and reaching the
            # exit
            if self.score == 3 and macgyver.finds_the_exit():
                self.win()
            # Check loosing condition: reaching the exit with at least one
            # missing object
            elif self.score < 3 and macgyver.finds_the_exit():
                self.loose()

    def display_msg(self, text):
        """Displays winning or loosing message at the end of the game"""
        # Define fonts
        smalltext = ch.st.pygame.font.Font('freesansbold.ttf', 20)
        largetext = ch.st.pygame.font.Font('freesansbold.ttf', 150)
        # Create an image (SURFACE) of the principal text, then blit this image
        # onto another SURFACE.
        textsurface = largetext.render(text, True, ch.st.WHITE)
        textrectangle = textsurface.get_rect()
        textrectangle.center = (ch.st.SURFACE_WIDTH / 2,
                                ch.st.SURFACE_HEIGHT / 2)
        ch.st.SURFACE.blit(textsurface, textrectangle)
        # Create an image (SURFACE) of the standard text, then blit this image
        # onto another SURFACE.
        textsurface = smalltext.render(
            'Press any key to continue', True, ch.st.WHITE)
        textrectangle = textsurface.get_rect()
        textrectangle.center = (ch.st.SURFACE_WIDTH / 2,
                                (ch.st.SURFACE_HEIGHT / 2) +
                                2 * ch.maze.sprite_dimension)
        ch.st.SURFACE.blit(textsurface, textrectangle)
        # Dispaly messages on the screen
        ch.st.pygame.display.update()
        # The message holds on the screen 2 seconds even if the player press
        # rapidely any key to continue as soon as macgyver arrives to the
        # finish position,
        time.sleep(3)

    def replay_or_quit(self):
        """Adapt the game to the player decision once the game is over:
        quitting or playing again"""
        for event in ch.st.pygame.event.get():
            if event.type == ch.st.pygame.QUIT:
                ch.st.pygame.quit()
                quit()
            elif event.type == ch.st.pygame.KEYDOWN:
                ch.st.SURFACE.fill(ch.st.BLACK)
                (macgyver.x, macgyver.y) = macgyver.start_position
                self.score = 0
                self.main()

    def win(self):
        """Displays winning message and invites the player to quit or replay"""
        self.display_msg("You win!")
        self.replay_or_quit()

    def loose(self):
        """Displays loosing message and invites the player to quit or replay"""
        self.display_msg("You loose!")
        self.replay_or_quit()

    def score_display(self):
        """Displays the score"""
        # Define fonts
        scoring_font = ch.st.pygame.font.Font('freesansbold.ttf', 16)
        # Create an image (SURFACE) of the principal text, then blit this image
        # onto another SURFACE.
        textsurface = scoring_font.render(
            "Score: " + str(self.score), True, ch.st.WHITE)
        textrectangle = textsurface.get_rect()
        textrectangle.center = ch.st.SURFACE_WIDTH - 2 * \
            ch.maze.sprite_dimension, ch.maze.sprite_dimension / 2
        # If the score changes, then erase the previous text
        # and blit the new one.
        # This condition will be maintained for score 1 and score 2 as they are
        # diffrent from 0
        if self.score != 0:
            textsurface.fill(ch.st.BLACK)
            ch.st.SURFACE.blit(textsurface, textrectangle)
            textsurface = scoring_font.render(
                "Score: " + str(self.score), True, ch.st.WHITE)

        ch.st.SURFACE.blit(textsurface, textrectangle)
        ch.st.pygame.display.update()
