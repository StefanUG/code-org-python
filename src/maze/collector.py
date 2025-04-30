import turtle
from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze


COLLECTOR_SHAPE = (
    (0, -15), (-5, -13), (-9, -8), (-9, 0), (-7, 5), (-9, 0), (-9, -8), (-5, -13), (-15, -12), (-19, -9), (-19, 0),
    (-16, 9), (-7, 5), (-16, 9), (-15, 13), (-9, 13), (-7, 11), (-7, 5), (0, 8), (7, 5), (7, 11), (9, 13), (15, 13),
    (16, 9), (7, 5), (16, 9), (19, 0), (19, -9), (15, -12), (5, -13), (9, -8), (9, 0), (7, 5), (9, 0), (9, -8),
    (5, -13), (0, -15))

class CollectorMazeType(MazeType):
  
    def __init__(self):
        super().__init__()
        self.cellClass = CollectorCell
        self.pathClass = CollectorPath
        self.playerClass = Collector
        self.subfolder = "collector"
        self.min_collected = -1

    def setup(self, level, maze: Maze):
        super().setup(level, maze)
        screen = maze.screen

        screen.bgcolor("dark grey")
        screen.register_shape(Maze.shapefile("crystal"))

        screen.register_shape(Maze.shapefile("wall_1"))
        screen.register_shape(Maze.shapefile("wall_2"))

        screen.register_shape(Maze.shapefile("floor_1"))
        screen.register_shape(Maze.shapefile("floor_2"))
        screen.register_shape(Maze.shapefile("floor_3"))
        screen.register_shape(Maze.shapefile("floor_4"))

        level_props = level['properties']
        min_col = level_props.get("min_collected")
        if min_col:
            self.min_collected = int(min_col)

    def detect_win_scenario(self, maze):
        return maze.player._gems_collected >= self.min_collected



class CollectorPath(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(90)
        self.penup()
        self.speed(0)

    def draw(self, x, y):
        self.x = x
        self.y = y
        self.goto(x, y)
        tile = random.randint(1, 4)
        self.shape(Maze.shapefile(f"floor_{tile}"))
        self.stamp()

class CollectorCell(Cell):

    def __init__(self,tileType=0, value=0, range=0, featureType=None):
        super().__init__(tileType=tileType, value=value, range=range)
        # Some levels have featureType in the serialized_maze field, even though Collector does not use it for anything

    def redraw(self):
        if self.is_wall():
            tile = random.randint(1, 2)
            self.showturtle()
            self.shape(Maze.shapefile(f"wall_{tile}"))

        if self.value != 0:
            self.shape(Maze.shapefile("crystal"))
            self.showturtle()
            self.draw_value()
        elif not self.is_wall():
            self.hideturtle()

        if self.originalValue != 0 and self.value == 0:
            # Clear any value that might have been previously written
            self.clear()

    def needs_visit(self):
        return self.originalValue > 0


class Collector(Player):

    def __init__(self, maze):
        super().__init__(maze)

        screen = self._turtle.getscreen()

        screen.register_shape("collector", COLLECTOR_SHAPE)

        self._turtle.color("black", "navajo white")
        self._turtle.shape("collector")

        self._gems_collected = 0

    def collect(self):
        self._process(lambda cell: cell.value > 0)
        self._gems_collected += 1
