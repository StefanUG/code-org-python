from enum import Enum
import turtle
import math
import random
import functools
import json
import os
import sys

_TESTMODE = os.environ.get('TESTMODE')

_TRACER_DELAY = 0 if _TESTMODE == "True" else 15
_TRACER_N = 0 if _TESTMODE == "True" else 1

# Get the directory of this Python file
_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("white")

    def draw_success(self):
        self.goto(0, 100)
        self.write("You did it!", False, "center", font=("Arial", 32, "bold"))

    def draw_failure(self):
        self.goto(0, 100)
        self.color("red")
        self.write("Oops, something is wrong", False, "center", font=("Arial", 28, "bold"))
        self.goto(0, 50)
        self.write("Try again!", False, "center", font=("Arial", 28, "bold"))

    def tick(self):
        self.getscreen().tracer(_TRACER_N, 50)
        self.left(1)
        self.right(2)
        self.left(1)
        self.getscreen().tracer(_TRACER_N, _TRACER_DELAY)


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.setheading(90)
        self.shape(Maze.shapefile("path"))
        self.color("brown")
        self.penup()
        self.speed(0)

    def draw(self, x, y):
        self.x = x
        self.y = y
        self.goto(x, y)
        self.stamp()


class Cell(turtle.Turtle):

    def __init__(self, tileType=0, value=0, range=0):
        super().__init__()
        self.tileType = SquareType(tileType)
        self.value = value
        self.originalValue = value
        self.range = range

        self.x = 0
        self.y = 0

        self.setheading(90)
        self.color("white")
        self.penup()
        self.speed(0)

        self.hideturtle()

    def is_variable_range(self):
        return self.value == self.originalValue and self.range != self.originalValue

    def draw(self, x, y):
        self.x = x
        self.y = y

        self.goto(x, y)

    def draw_value(self):
        value = abs(self.value)
        if self.is_variable_range():
            value = '?'

        delay = self.getscreen().delay()
        if delay:
            self.getscreen().tracer(0, 0)
        self.clear()
        self.setpos(self.x + 20, self.y - 20)
        self.write(value, False, align="right", font=("Arial", 18, "bold"))
        self.setpos(self.x, self.y)
        if delay:
            self.getscreen().tracer(_TRACER_N, delay)

    def needs_visit(self):
        return self.tileType.is_open()

    def is_open(self):
        return self.tileType.is_open()

    def is_obstacle(self):
        return self.tileType.is_obstacle()

    def is_finish(self):
        return self.tileType.is_finish()

    @staticmethod
    def sort_list(the_list):
        the_list.sort(key=lambda cell: (cell.x, cell.y))

    def redraw(self):
        """
        Method that will be called when the player moved, so the cell has a chance to redraw itself if needed
        :return:
        """


class SquareType(Enum):
    WALL = 0
    OPEN = 1
    START = 2
    FINISH = 3
    OBSTACLE = 4
    STARTANDFINISH = 5

    def is_open(self):
        return self.value > 0

    def is_obstacle(self):
        return self == SquareType.OBSTACLE

    def is_wall(self):
        return self.value == 0

    def is_start(self):
        return self in [SquareType.START, SquareType.STARTANDFINISH]

    def is_finish(self):
        return self in [SquareType.FINISH, SquareType.STARTANDFINISH]


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @classmethod
    def _missing_(cls, value):
        value = int(value)
        for member in cls:
            if member.value == value:
                return member
        return None

    def left(self):
        value = self.value - 1
        if value < 0:
            value = 3
        return Direction(value)

    def right(self):
        value = self.value + 1
        if value > 3:
            value = 0
        return Direction(value)

    def to_heading(self):
        """
        Converts the direction of a Maze level to python turtle "standard" mode
          0 - east      1
         90 - north     0
        180 - west      3
        270 - south     2
        """
        if self == Direction.NORTH:
            return 90
        elif self == Direction.SOUTH:
            return 270
        elif self == Direction.WEST:
            return 180

        return 0

    @staticmethod
    def from_heading(head):
        """
        Returns a Direction based on the heading in degrees
        """
        if head == 90:
            return Direction.NORTH
        elif head == 270:
            return Direction.SOUTH
        elif head == 180:
            return Direction.WEST

        return Direction.EAST


class MazeType:

    def __init__(self):
        super().__init__()
        self.subfolder = None

        self.pathClass = Path
        self.cellClass = Cell
        self.playerClass = Player

        self._path = None

    def new_player(self, maze):
        return self.playerClass(maze)

    def new_cell(self, cell_dict) -> Cell:
        return self.cellClass(**cell_dict)

    def path(self):
        if self._path is None:
            self._path = self.pathClass()
        return self._path

    def setup(self, level, screen):
        """
        Method is called before starting to render and setup the Maze
        """

    def after_move(self, maze):
        """
        Method is called after each move, to handle any actions that are needed
        """
        if hasattr(self.cellClass, "reveal"):
            coords = maze.player.gridcoords()
            maze.get_cell((coords[0], coords[1])).reveal()
            if coords[1] > 0:  # reveal above
                maze.get_cell((coords[0], coords[1] - 1)).reveal()
            if coords[0] > 0:  # reveal left
                maze.get_cell((coords[0] - 1, coords[1])).reveal()
            if coords[1] < len(maze.grid) - 1:  # reveal below
                maze.get_cell((coords[0], coords[1] + 1)).reveal()
            if coords[0] < len(maze.grid[coords[1]]) - 1:  # reveal right
                maze.get_cell((coords[0] + 1, coords[1])).reveal()

    def parse_cell_from_old_values(self, map_cell, initial_dirt_cell):
        """
        Simplest method to parse the cell
        """
        map_cell = str(map_cell)
        if initial_dirt_cell:
            initial_dirt_cell = int(initial_dirt_cell)

        tile_type = int(map_cell)
        value = initial_dirt_cell

        return dict(tileType=tile_type, value=value)

    def success(self, maze, player):
        player._success()

    def failure(self, maze, player):
        player._fail()


class Maze:

    @staticmethod
    def _testmode():
        global _TRACER_DELAY
        global _TRACER_N
        _TRACER_DELAY = 0
        _TRACER_N = 0

    @staticmethod
    def shapefile(name: str, ext: str = ".gif") -> str:
        name = os.path.join(Maze.instance.maze_type.subfolder, name)
        return os.path.join(_DIR_PATH, "images", name + ext)

    instance = None

    def __init__(self, level: dict, maze_type: MazeType):
        Maze.instance: Maze = self
        self.maze_type: MazeType = maze_type

        self.screen = turtle.Screen()
        self.walls = []
        self.player = None
        self.path = None

        self.width = 0
        self.height = 0

        self.grid = []

        self.cells_to_visit = []
        self.visited = []

        self.pen = Pen()

        maze_type.setup(level, self.screen)

        self.screen.bgcolor("white")
        self.screen.setup(410, 410)  # TODO Add dynamic size
        self.screen.tracer(0, 0)

        self._setup_maze(level)

        self.pen.tick()

    def parse_maze(self, level_props):
        maze = json.loads(level_props["maze"])
        initial_dirt_matrix = level_props.get("initial_dirt")
        initial_dirt = None
        if initial_dirt_matrix:
            initial_dirt = json.loads(initial_dirt_matrix)

        parsed_maze = []
        for r in range(len(maze)):
            row = []
            parsed_maze.append(row)
            for c in range(len(maze[r])):
                cell = self.maze_type.parse_cell_from_old_values(maze[r][c],
                                                                 initial_dirt[r][c] if initial_dirt else None)
                row.append(cell)

        return parsed_maze

    def _setup_maze(self, level):
        level_props = level['properties']

        step_speed = level_props.get("step_speed")

        if step_speed and not _TESTMODE:
            global _TRACER_DELAY
            _TRACER_DELAY = 15 / int(step_speed)

        maze = None
        if level_props.get("serialized_maze"):
            maze = json.loads(level_props.get("serialized_maze"))

        if not maze:
            maze = self.parse_maze(level_props)

        rows = len(maze)
        self.height = rows * 50
        self.grid = []

        for y in range(rows):
            row = []
            self.grid.append(row)
            cols = len(maze[y])
            for x in range(cols):
                if self.width == 0:
                    self.width = cols * 50

                cell = self.maze_type.new_cell(maze[y][x])
                row.append(cell)

                screen_x = -1 * ((self.width / 2) - 25) + (x * 50)
                screen_y = (self.height / 2 - 25) - (y * 50)

                if cell.tileType.is_open():
                    if self.maze_type.path():
                        self.maze_type.path().draw(screen_x, screen_y)
                    if cell.needs_visit():
                        self.cells_to_visit.append(cell)

                cell.draw(screen_x, screen_y)

                if cell.tileType == SquareType.WALL:
                    self.walls.append((x, y))

                if cell.tileType.is_start():
                    self.startCell = cell

        self.maze_type.path().hideturtle()
        Cell.sort_list(self.cells_to_visit)

        self.player = self.maze_type.new_player(self)
        self.player._turtle.goto(self.startCell.x, self.startCell.y)

        direction = level_props.get("start_direction")
        if direction:
            direction = Direction(direction)
            self.player._turtle.setheading(direction.to_heading())

        self.update()

    def update(self):
        coords = self.player.gridcoords()
        cell = self.get_cell(coords)
        if not cell in self.visited:
            self.visited.append(cell)
            Cell.sort_list(self.visited)

        self.maze_type.after_move(self)

        self.pen.tick()

    def done(self):
        if self.detect_win_scenario():
            self._success()
        else:
            self._fail()

    def _success(self):
        self.maze_type.success(self, self.player)

    def _fail(self):
        self.maze_type.failure(self, self.player)

    def detect_win_scenario(self):
        if all(element in self.visited for element in self.cells_to_visit):
            value = self.get_cell_values()
            return value == 0
        return False

    def get_cell_values(self):
        return functools.reduce(lambda v, cell: v + (cell.value if cell.value else 0), self.visited, 0)

    def get_cell(self, gridcoords: (int, int)) -> Cell:
        row = None
        if len(self.grid) > gridcoords[1] >= 0:
            row = self.grid[gridcoords[1]]
        if row is not None and len(row) > gridcoords[0] >= 0:
            return row[gridcoords[0]]
        return None

    def is_wall(self, gridcoords):
        cell = self.get_cell(gridcoords)
        return cell.tileType.is_wall()

    def is_path_in_heading(self, start_yx, heading):
        cell: Cell = None
        if heading == Direction.NORTH.to_heading():
            cell = self.get_cell((start_yx[0], start_yx[1] - 1))
        elif heading == Direction.EAST.to_heading():
            cell = self.get_cell((start_yx[0] + 1, start_yx[1]))
        elif heading == Direction.SOUTH.to_heading():
            cell = self.get_cell((start_yx[0], start_yx[1] + 1))
        elif heading == Direction.WEST.to_heading():
            cell = self.get_cell((start_yx[0] - 1, start_yx[1]))

        return cell is not None and cell.is_open()


class Player:
    maze: Maze = None
    instance = None

    _turtle = turtle.Turtle()

    def __init__(self, maze):
        Player.instance = self
        self.maze = maze

        self._turtle.penup()
        self._turtle.speed(1)

    def is_collision(self, other):
        a = self._turtle.xcor() - other.turtle.xcor()
        b = self._turtle.ycor() - other.turtle.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

    def gridcoords(self):
        """Return the turtle's current location witin the grid system (col,row), as a Vec2D-vector.

        No arguments.

        Example (for a Turtle instance named pegman):
        >>> pegman.pos()
        (1, 8)
        """
        col = round((self.maze.width / 2 + (self._turtle.xcor() - 25)) / 50)
        row = round((self.maze.height / 2 - (self._turtle.ycor() + 25)) / 50)
        return col, row

    def _get_current_cell(self) -> Cell:
        return self.maze.get_cell(self.gridcoords())

    def _check(self):
        if self.maze.is_wall(self.gridcoords()):
            self._fail()

        self.maze.update()

    def _fail(self, undo=True):
        print("fail")
        if _TRACER_N > 0:
            if (undo):
                self._turtle.undo()
            self._turtle.color("black", "red")
            self.maze.pen.draw_failure()
            self._turtle.getscreen().mainloop()

    def _success(self):
        print("success")
        if _TRACER_N > 0:
            self.maze.pen.draw_success()
            self._turtle.speed(8)
            self._turtle.right(360)
            self._turtle.left(360)
            self._turtle.getscreen().mainloop()

    def _process(self, cond, deduct=1):
        color = self._turtle.color()
        self._turtle.color("black", "orange")
        cell = self._get_current_cell()
        if cond(cell):
            if (deduct > 0 >= cell.value) or (deduct < 0 <= cell.value):
                self._fail()
            cell.value -= deduct
            cell.redraw()
        else:
            self._fail()

        self._turtle.color(color[0], color[1])

    def _get_value_if(self, cell_condition):
        cell = self._get_current_cell()
        value = 0
        if cell_condition(cell):
            value = cell.value
        return value

    def forward(self, steps=1):
        for i in range(steps):
            self._turtle.forward(50)
            self._check()

    def backward(self, steps=1):
        for i in range(steps):
            self._turtle.backward(50)
            self._check()

    move_forward = forward
    go_forward = forward

    def right(self):
        self._turtle.right(90)

    def left(self):
        self._turtle.left(90)

    def path_ahead(self):
        coords = self.gridcoords()
        head = self._turtle.heading()
        return self.maze.is_path_in_heading(coords, head)

    def path_left(self):
        coords = self.gridcoords()
        d = Direction.from_heading(self._turtle.heading()).left()
        return self.maze.is_path_in_heading(coords, d.to_heading())

    def path_right(self):
        coords = self.gridcoords()
        d = Direction.from_heading(self._turtle.heading()).right()
        return self.maze.is_path_in_heading(coords, d.to_heading())

    def at_finish(self):
        """
        Is the player at the finish point yet?
        :return:
        """
        return self._get_current_cell().is_finish()
