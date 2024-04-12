from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze


BIRD_SHAPE = ((0,-12),(-1,-12),(-2,-10),(-3,-3),(-4,-1),(-10,3),(-20,3),(-24,4),(-11,9),(-8,9),(-3,7),(0,10),(0,10),
              (3,7),(8,9),(11,9),(24,4),(20,3),(10,3),(4,-1),(3,-3),(2,-10),(1,-12),(0,-12))


class BirdsMazeType(MazeType):
  
    def __init__(self):
        super().__init__()
        self.cellClass = BirdsCell
        self.playerClass = Bird
        self.subfolder = "birds"

    def setup(self, level, maze):
        super().setup(level, maze)
        screen = maze.screen

        screen.bgpic(Maze.shapefile("background", ".png"))
        screen.register_shape(Maze.shapefile("path"))
        screen.register_shape(Maze.shapefile("tnt"))
        screen.register_shape(Maze.shapefile("monster"))

        screen.register_shape(Maze.shapefile("wall_1"))
        screen.register_shape(Maze.shapefile("wall_2"))
        screen.register_shape(Maze.shapefile("wall_3"))
        screen.register_shape(Maze.shapefile("wall_4"))
        screen.register_shape(Maze.shapefile("wall_5"))

        self.path()._stamp = False


class BirdsCell(Cell):

    def __init__(self,tileType=0, value=0, range=0):
        super().__init__(tileType=tileType, value=value, range=range)

    def redraw(self):
        if self.is_obstacle():
            self.shape(Maze.shapefile("tnt"))
        elif self.is_finish():
            self.shape(Maze.shapefile("monster"))
        elif self.is_wall():
            tile = random.randint(1, 5)
            self.shape(Maze.shapefile(f"wall_{tile}"))

        if self.tileType in [SquareType.OPEN, SquareType.START]:
            self.hideturtle()
        else:
            self.showturtle()

    def needs_visit(self):
        return self.is_finish()


class Bird(Player):

    def __init__(self, maze):
        super().__init__(maze)

        screen = self._turtle.getscreen()

        screen.register_shape("bird", BIRD_SHAPE)

        self._turtle.color("black","red")
        self._turtle.shape("bird")
