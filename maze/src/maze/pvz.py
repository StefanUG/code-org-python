from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze


ZOMBIE_SHAPE = ((0,-15),(-5,-13),(-9,-8),(-9, 0),(-7, 5),(-9, 0),(-9,-8),(-5,-13),(-15,-12),(-19,-9),(-19,0),(-16,9),(-7,5),(-16,9),(-15,13),(-9,13),(-7,11),(-7,5),(0,8),(7,5),(7,11),(9,13),(15,13),(16,9),(7,5),(16,9),(19,0),(19,-9),(15,-12),(5,-13),(9,-8),(9, 0),(7, 5),(9, 0),(9,-8),(5,-13),(0,-15))


class ZombieMazeType(MazeType):
  
    def __init__(self):
        super().__init__()
        self.cellClass = ZombieCell
        self.playerClass = ZombiePlayer
        self.subfolder = "pvz"

    def setup(self, level, screen):
        super().setup(level, screen)
        screen.bgpic(Maze.shapefile("background"))
        screen.register_shape(Maze.shapefile("path"))
        screen.register_shape(Maze.shapefile("obstacle"))
        screen.register_shape(Maze.shapefile("flower"))


class ZombieCell(Cell):

    def __init__(self,tileType=0, value=0, range=0):
        super().__init__(tileType=tileType, value=value, range=range)

    def draw(self, x, y):
        super().draw(x, y)
        self.redraw()

    def redraw(self):
        if self.is_obstacle():
            self.shape(Maze.shapefile("obstacle"))
            self.showturtle()
        elif self.is_finish():
            self.shape(Maze.shapefile("flower"))
            self.showturtle()

    def needs_visit(self):
        return self.is_finish()


class ZombiePlayer(Player):

    def __init__(self, maze):
        super().__init__(maze)

        screen = self._turtle.getscreen()

        screen.register_shape("zombie", ZOMBIE_SHAPE)

        self._turtle.color("brown","green")
        self._turtle.shape("zombie")

    def _check(self):
        super()._check()
        if self._get_current_cell().is_finish():
            self._success()
