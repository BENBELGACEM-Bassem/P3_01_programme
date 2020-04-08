# This module contains classess responsible for creating game characters

from random import sample

import structure as st

# Create maze instance
maze = st.Structure()


class Hero:
    """Generates hero instance and controls his mouvements"""
    def __init__(self):
        """Define properties of the hero"""
        self.width = 32
        self.height = 40
        # Putting MacGyver at the center of the entrance spot
        self.distance_to_horizontal_edge = (
            maze.sprite_dimension - self.width) / 2
        self.distance_to_vertical_edge = (
            maze.sprite_dimension - self.height) / 2
        self.x = maze.entrance[0][0] + self.distance_to_horizontal_edge
        self.y = maze.entrance[0][1] + self.distance_to_vertical_edge
        # MacGyver move by a step equal to sprite dimension
        self.speed = maze.sprite_dimension
        self.image = st.pygame.image.load("MacGyver.png")
        self.start_position = (self.x, self.y)

    # The following functions define four possible mouvements.
    # Each mouvement function, draws a BLACK rectangle in the previous position
    # This will allow to hide objects after collecting them
    def moves_up(self):
        """Once called the hero moves up and prvious position becomes BLACK"""
        st.pygame.draw.rect(
            st.SURFACE,
            st.BLACK,
            (self.x,
             self.y,
             self.width,
             self.height))
        self.y -= self.speed

    def moves_down(self):
        """Once called hero moves down and prvious position becomes BLACK"""
        st.pygame.draw.rect(
            st.SURFACE,
            st.BLACK,
            (self.x,
             self.y,
             self.width,
             self.height))
        self.y += self.speed

    def moves_right(self):
        """Once called hero moves right and prvious position becomes BLACK"""
        st.pygame.draw.rect(
            st.SURFACE,
            st.BLACK,
            (self.x,
             self.y,
             self.width,
             self.height))
        self.x += self.speed

    def moves_left(self):
        """Once called hero moves left and prvious position becomes BLACK"""
        st.pygame.draw.rect(
            st.SURFACE,
            st.BLACK,
            (self.x,
             self.y,
             self.width,
             self.height))
        self.x -= self.speed

    def nearest_left_spot_empty(self):
        """Returns True if the nearest left (x,y) couple to the hero, is within
        passage_positions list,containing empty spots of the maze"""
        return ((self.x - (self.distance_to_horizontal_edge +
                maze.sprite_dimension)),
                (self.y -
                 self.distance_to_vertical_edge)) in maze.passage_positions

    def nearest_right_spot_empty(self):
        """Returns True if the nearest right (x,y) couple to the hero, is within
        passage_positions list,containing empty spots of the maze"""
        return (((self.x + maze.sprite_dimension -
                 self.distance_to_horizontal_edge),
                (self.y - self.distance_to_vertical_edge)) in
                maze.passage_positions)

    def nearest_upper_spot_empty(self):
        """Returns True if the nearest upper (x,y) couple to the hero, is within
        passage_positions list,containing empty spots of the maze"""
        return ((self.x -
                 self.distance_to_horizontal_edge), self.y -
                (self.distance_to_vertical_edge +
                 maze.sprite_dimension)) in maze.passage_positions

    def nearest_lower_spot_empty(self):
        """Returns True if the nearest lower (x,y) couple to the hero, is within
        passage_positions list,containing empty spots of the maze"""
        return ((self.x -
                 self.distance_to_horizontal_edge), self.y +
                maze.sprite_dimension -
                self.distance_to_vertical_edge) in maze.passage_positions

    def picks_up(self, object):
        """Returns True if the hero reachs the position of an object"""
        return (
            self.x -
            self.distance_to_horizontal_edge,
            self.y -
            self.distance_to_vertical_edge) == (
            object.x -
            object.distance_to_horizontal_edge,
            object.y -
            object.distance_to_vertical_edge)

    def finds_the_exit(self):
        """Returns True if the hero reachs the maze exit"""
        return [(self.x - self.distance_to_horizontal_edge,
                 self.y - self.distance_to_vertical_edge)] == maze.exit


class Enemy:
    """Generates enemy instance and controls his position"""
    def __init__(self):
        self.width = 32
        self.height = 36
        self.x = maze.enemy_location[0][0] + \
            (maze.sprite_dimension - self.width) / 2
        self.y = maze.enemy_location[0][1] + \
            (maze.sprite_dimension - self.height) / 2
        self.position = (self.x, self.y)
        self.image = st.pygame.image.load("Gardien.png")


class Object:
    """Generates objects instances and controls its positions"""
    # Fixing the number of objects to three via this class attribute Number
    Number = 3
    # Using sample function to insure getting
    # three different couples of coordinates (x,y)
    # from the object locations list
    # Make this property a class property, so it is not recreated with each
    # instance to avoid a possible case where two or more objects are in the
    # same location
    random_positions = sample(maze.objects_locations, Number)

    def __init__(self, index, image):
        """Defines object attributes"""
        # Limit the object index to 0,1 or 2 as there are 3 objects to gather
        if index not in range(Object.Number):
            raise ValueError(
                "Please enter a value in" + list(range(Object.Number)))
        self.index = index
        self.image = st.pygame.image.load(image)
        self.width = 30
        self.height = 30
        self.distance_to_horizontal_edge = (
            maze.sprite_dimension - self.width) / 2
        self.distance_to_vertical_edge = (
            maze.sprite_dimension - self.height) / 2
        # Choose randomly, three (x,y) couples from empty spot of the maze.
        # Then,depending on the object index, assign an (x,y)
        # from this list to this object
        # Center the object in the empty spot
        self.x = Object.random_positions[self.index][0] + \
            self.distance_to_horizontal_edge
        self.y = Object.random_positions[self.index][1] + \
            self.distance_to_vertical_edge
        self.position = (self.x, self.y)
