from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze

FARMER_SHAPE = (
    (0, -15), (-5, -13), (-9, -8), (-9, 0), (-7, 5), (-9, 0), (-9, -8), (-5, -13), (-15, -12), (-19, -9), (-19, 0),
    (-16, 9), (-7, 5), (-16, 9), (-15, 13), (-9, 13), (-7, 11), (-7, 5), (0, 8), (7, 5), (7, 11), (9, 13), (15, 13),
    (16, 9), (7, 5), (16, 9), (19, 0), (19, -9), (15, -12), (5, -13), (9, -8), (9, 0), (7, 5), (9, 0), (9, -8),
    (5, -13), (0, -15))


class FarmerMazeType(MazeType):

    def __init__(self):
        super().__init__()
        self.cellClass = FarmerCell
        self.playerClass = Farmer
        self.subfolder = "farmer"

    def setup(self, level, screen):
        super().setup(level, screen)
        screen.bgpic(Maze.shapefile("background", ".png"))
        screen.register_shape(Maze.shapefile("path"))
        screen.register_shape(Maze.shapefile("hole"))
        screen.register_shape(Maze.shapefile("pile"))

    def success(self, maze, player):
        self.path().clear()
        super().success(maze, player)


class FarmerCell(Cell):

    def __init__(self, tileType=0, value=0, range=0, featureType=0):
        super().__init__(tileType=tileType, value=value, range=range)

    def redraw(self):
        if self.value != 0:
            if self.is_hole():
                self.shape(Maze.shapefile("hole"))
            else:
                self.shape(Maze.shapefile("pile"))
            self.showturtle()
        else:
            self.hideturtle()

        if self.value != 0:
            self.draw_value()

        if self.originalValue != 0 and self.value == 0:
            # Clear any value that might have been previously written
            self.clear()

    def is_hole(self):
        return self.value < 0

    def is_pile(self):
        return self.value > 0

    def needs_visit(self):
        return self.originalValue != 0


class Farmer(Player):

    def __init__(self, maze):
        super().__init__(maze)

        screen = self._turtle.getscreen()

        screen.register_shape("farmer", FARMER_SHAPE)

        self._turtle.color("black", "steel blue")
        self._turtle.shape("farmer")

    def remove(self):
        """
        Removes dirt from a pile
        :return:
        """
        self._process(lambda cell: cell.is_pile())

    def fill(self):
        """
        Fills the hole with dirt
        :return:
        """
        self._process(lambda cell: cell.is_hole(), -1)

    def at_pile(self):
        return self._get_current_cell().is_pile()

    def at_hole(self):
        return self._get_current_cell().is_hole()
