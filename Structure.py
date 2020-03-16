''' This module contains the pygame boiler plate to initiate pygame module and
the Structure class to create the maze'''

import pygame

# Pygame boiler plate
pygame.init()
surface_width = 770
surface_height = 770
surface = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption("Escape_game")
clock = pygame.time.Clock()
# Define colors that will be used
White = (255, 255, 255)
Black = (0, 0, 0)


class Structure:

    ''' The class Structure contains needed function and properties
    to define the maze '''

    def __init__(self):
        '''Define properties of the maze'''
        self.sprite_dimension = 45
        self.map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 1, 1, 1, "E", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                    [2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                    [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
                    [2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 2],
                    [2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2],
                    [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
                    [2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 2],
                    [2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2],
                    [2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 2],
                    [2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 2],
                    [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 2],
                    [2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 2],
                    [2, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                    [2, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2],
                    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "S", 1, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "G", 2, 2]]

        self.entrance = [(column * self.sprite_dimension,
                         row * self.sprite_dimension)
                         for row in range(len(self.map))
                         for column in range(len(self.map[row]))
                         if self.map[row][column] == "E"]
        self.exit = [(column * self.sprite_dimension,
                     row * self.sprite_dimension)
                     for row in range(len(self.map))
                     for column in range(len(self.map[row]))
                     if self.map[row][column] == "S"]

    def draw_maze(self, surface, sprite):
        '''Once called, this functopn will draw the Maze'''
        image = pygame.image.load(sprite)
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == 1:
                    surface.blit(image,
                                 (column * self.sprite_dimension,
                                  row * self.sprite_dimension))

    @property
    def objects_locations(self):
        '''Define the empty positions inside the Maze for objects'''
        objects_locations = []
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == 0:
                    objects_locations.append(
                        (column * self.sprite_dimension,
                         row * self.sprite_dimension))
        return objects_locations

    @property
    def passage_positions(self):
        ''' Define the empty positions inside the Maze for MacGyver'''
        passage_positions = [(column * self.sprite_dimension,
                             row * self.sprite_dimension)
                             for row in range(len(self.map))
                             for column in range(len(self.map[row]))
                             if (self.map[row][column] == 0 or
                                 self.map[row][column] == "E"or
                                 self.map[row][column] == "S")]
        return passage_positions

    @property
    def enemy_location(self):
        '''Define the empty positions inside the Maze for the guardian'''
        enemy_location = []
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == "G":
                    enemy_location.append((column * self.sprite_dimension,
                                          row * self.sprite_dimension))
        return enemy_location
