# This module contains the pygame boiler plate to initiate pygame module
# and the Structure class to create the maze
from json import loads

import pygame


# Pygame boiler plate
pygame.init()
SURFACE_WIDTH = 770
SURFACE_HEIGHT = 770
SURFACE = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
pygame.display.set_caption("Escape_game")
CLOCK = pygame.time.Clock()
# Define colors that will be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Structure:

    """The class Structure contains needed function and properties
    to define the maze"""

    def __init__(self):
        """Define properties of the maze"""
        self.sprite_dimension = 45
        # Import the labyrinth matrix from a dedicated file
        # in way that makes it a nested list
        with open('labyrinth.txt', 'r') as f:
            string_enclosed_list = [line.strip() for line in f.readlines()]
            self.map = [loads(row) for row in string_enclosed_list]

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

    def draw_maze(self, SURFACE, sprite):
        """Once called, this functopn will draw the Maze"""
        image = pygame.image.load(sprite)
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == 1:
                    SURFACE.blit(image,
                                 (column * self.sprite_dimension,
                                  row * self.sprite_dimension))

    @property
    def objects_locations(self):
        """Define the empty positions inside the Maze for objects"""
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
        """Define the empty positions inside the Maze for MacGyver"""
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
        """Define the empty positions inside the Maze for the guardian"""
        enemy_location = []
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == "G":
                    enemy_location.append((column * self.sprite_dimension,
                                          row * self.sprite_dimension))
        return enemy_location
