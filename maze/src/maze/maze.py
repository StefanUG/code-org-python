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
_TRACER_N     = 0 if _TESTMODE == "True" else 1

"""
Global functions to make it easier to code the solutions
"""

def forward(steps=1):
  Player.instance.go_forward(steps)

def right():
  Player.instance.right()

def left():
  Player.instance.left()

def at_flower():
  return Player.instance.at_flower()

def at_honeycomb():
  return Player.instance.at_hive()

at_hive = at_honeycomb

def done():
  Maze.instance.done()



class Pen(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.penup()
    self.color("white")

  def draw_success(self):
    self.goto(0, 100)
    self.write("You did it!", False, "center", font=("Arial", "32", "bold"))

  def draw_failure(self):
    self.goto(0, 100)
    self.color("red")
    self.write("Oops, something is wrong", False, "center", font=("Arial", "28", "bold"))
    self.goto(0, 50)
    self.write("Try again!", False, "center", font=("Arial", "28", "bold"))
    

  def tick(self):
    self.getscreen().tracer(_TRACER_N,50)
    self.left(1)
    self.right(2)
    self.left(1)
    self.getscreen().tracer(_TRACER_N,_TRACER_DELAY)

    

class Wall(turtle.Turtle):
  def  __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("green")
    self.penup()
    self.speed(0)

class Path(turtle.Turtle):
  def  __init__(self):
    turtle.Turtle.__init__(self)
    self.setheading(90)
    self.shape(_shapefile("earth"))
    self.color("brown")
    self.penup()
    self.speed(0)

  def draw(self, x, y):
    self.x = x
    self.y = y
    self.goto(x, y)
    self.stamp()

class Cell(turtle.Turtle):
  tileType = 0
  originalValue = 0
  currentValue = 0
  value = 0
  range = 0

  x = 0
  y = 0

  def __init__(self, tileType=0, value=0, range=0):
    super().__init__()
    self.tileType = SquareType(tileType)
    self.value = value
    self.originalValue = value
    self.range = range

    self.setheading(90)
    self.color("white")
    self.penup()
    self.speed(0)

    self.hideturtle()
      

  def draw(self, x, y):
    self.x = x
    self.y = y

    self.goto(x, y)

  def drawValue(self):
    delay = self.getscreen().delay()
    if (delay):
      self.getscreen().tracer(0,0)
    self.clear()
    self.setpos(self.x+20, self.y-20)
    self.write(self.value, False, align="right", font=("Arial", "18", "bold"))
    self.setpos(self.x, self.y)
    if (delay):
      self.getscreen().tracer(_TRACER_N,delay)

  def needs_visit(self):
    return self.tileType.isOpen()

  def isOpen(self):
    return self.tileType.isOpen()

  @staticmethod
  def sort_list(list):
    list.sort(key=lambda cell: (cell.x, cell.y))


class SquareType(Enum):
  WALL = 0
  OPEN = 1
  START = 2
  FINISH = 3
  OBSTACLE = 4
  STARTANDFINISH = 5

  def isOpen(self):
    return self.value > 0
  
  def isWall(self):
    return self.value == 0

  def isStart(self):
    return self in [SquareType.START, SquareType.STARTANDFINISH]


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

  def to_heading(self):
    """
    Converts the direction of a Maze level to python turtle "standard" mode
      0 - east      1
    90 - north     0
    180 - west      3
    270 - south     2
    """
    if (self == Direction.NORTH):
      return 90
    elif (self == Direction.SOUTH):
      return 270
    elif (self == Direction.WEST):
      return 180
    
    return 0


###
### Harvester Stuff
###
class HarvesterFeatureType(Enum):
  NONE = 0
  CORN = 1
  PUMPKIN = 2
  LETTUCE = 3


class MazeType():

  cellClass = None
  playerClass = None

  def __init__(self, cellClass, playerClass):
    super().__init__()
    self.cellClass = cellClass
    self.playerClass = playerClass

  def newPlayer(self, maze):
    return self.playerClass(maze)
  
  def newCell(self, cellDict):
    return self.cellClass(**cellDict)
  
  def setup(self, level, screen):
    """
    Dummy method to be implemented by subclass
    """
    return
  
  def parse_cell_from_old_values(mapCell, initialDirtCell):
    """
    Dummy method to be implemented by subclass
    """
    return


class Maze:

  @staticmethod
  def _testmode():
    global _TRACER_DELAY
    global _TRACER_N
    _TRACER_DELAY = 0
    _TRACER_N = 0

  mazeType = None

  name = None
  screen = turtle.Screen()
  treasures = []
  walls = []
  player = None
  path = None

  width = 0
  height = 0
  
  cellType = Cell

  grid = []

  cells_to_visit = []
  visited = []

  pen = None

  def __init__(self, level, mazeType):
    Maze.instance = self
    self.mazeType = mazeType

    levelProps = level['properties']

    mazeType.setup(level)

    self.screen.bgcolor("white")
    self.screen.setup(410,410)
    self.screen.tracer(0,0)
    self.screen.bgpic(_shapefile(levelProps['skin'] + "_background", ".png"))

    self.screen.register_shape(_shapefile("cloud"))
    self.screen.register_shape(_shapefile("earth"))
    self.screen.register_shape(_shapefile("hole"))
    self.screen.register_shape(_shapefile("pile"))
    self.screen.register_shape(_shapefile("purple_flower"))
    self.screen.register_shape(_shapefile("red_flower"))
    self.screen.register_shape(_shapefile("honeycomb"))

    if (levelProps['skin'] == 'bee'):
      self.cellType = BeeCell
      self.path = Path()

    self._setup_maze(level)

    self.pen.tick()
  
  def parse_maze(self, levelProps):
    maze = json.loads(levelProps["maze"])
    initialDirt = json.loads(levelProps["initial_dirt"])

    parsed_maze = []
    for r in range(len(maze)):
      row = []
      parsed_maze.append(row)
      for c in range(len(maze[r])):
        cell = self.type.parse_cell_from_old_values(maze[r][c], initialDirt[r][c])
        row.append(cell)

    return parsed_maze


  def _setup_maze(self, level):
    levelProps = level['properties']
    
    maze = None
    if levelProps.get("serialized_maze"):
      maze = json.loads(levelProps.get("serialized_maze"))

    if not maze:
      maze = self._parse_maze(levelProps)

    rows = len(maze)
    self.height = rows * 50
    self.grid = []
    self.pen = Pen()

    for y in range(rows):
      row = []
      self.grid.append(row)
      cols = len(maze[y])
      for x in range(cols):
        if (self.width == 0):
          self.width = cols * 50

        cell = self.cellType(**maze[y][x])
        row.append(cell)

        screen_x = -1*((self.width/2)-25) + (x * 50)
        screen_y = (self.height/2-25) - (y * 50)

        if (cell.tileType.isOpen()):
          if (self.path):
            self.path.draw(screen_x, screen_y)
          if (cell.needs_visit()):
            self.cells_to_visit.append(cell)
        
        cell.draw(screen_x, screen_y)

        if (cell.tileType == SquareType.WALL):
          self.walls.append((x, y))

        if (cell.tileType.isStart()):
          self.startCell = cell

    Cell.sort_list(self.cells_to_visit)

    self.player = Player(self)
    self.player.turtle.goto(self.startCell.x, self.startCell.y)

    dir = levelProps.get("start_direction")
    if (dir):
      dir = Direction(dir)
      self.player.turtle.setheading(dir.to_heading())

    self.update()


  def update(self):
    coords = self.player.gridcoords()
    cell = self.getCell(coords)
    if (not cell in self.visited):
      self.visited.append(cell)
      Cell.sort_list(self.visited)
      
    self.getCell((coords[0], coords[1])).reveal()
    if (coords[1] > 0): # reveal above
      self.getCell((coords[0], coords[1]-1)).reveal()
    if (coords[0] > 0): # reveal left
      self.getCell((coords[0]-1, coords[0])).reveal()
    if (coords[1] < len(self.grid)-1): # reveal below
      self.getCell((coords[0], coords[1]+1)).reveal()
    if (coords[0] < len(self.grid[coords[1]])-1): # reveal right
      self.getCell((coords[0]+1, coords[1])).reveal()


    self.pen.tick()


  def done(self):
    if (self.detectWinScenario()):
      self.player._success()
    else:
      self.player._fail(False)
  
  def detectWinScenario(self):
    if (all(element in self.visited for element in self.cells_to_visit)):
      value = self.get_cell_values()
      return value == 0
    return False
  
  def get_cell_values(self):
      return functools.reduce(lambda v, cell: v + cell.value, self.visited, 0)



  def getCell(self, gridcoords):
    row = None
    if (len(self.grid) > gridcoords[1] and gridcoords[1] >= 0):
      row = self.grid[gridcoords[1]]
    if (row is not None and len(row) > gridcoords[0] and gridcoords[0] >= 0):
      return row[gridcoords[0]]
    return None

  def isWall(self, gridcoords):
    cell = self.getCell(gridcoords)
    return cell.tileType.isWall()


class Player():
  maze:Maze = None
  instance = None

  _turtle = turtle.Turtle()

  def __init__(self, maze):
    Player.instance = self
    self.maze = maze

    self._turtle.penup()
    self._turtle.speed(1)

    self.at_hive = self.at_honeycomb

  def is_collision(self, other):
    a = self._turtle.xcor()-other.turtle.xcor()
    b = self._turtle.ycor()-other.turtle.ycor()
    distance = math.sqrt((a**2)+(b**2))

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
    col = round((self.maze.width/2  + (self._turtle.xcor()-25)) / 50)
    row = round((self.maze.height/2 - (self._turtle.ycor()+25) ) / 50)
    return (col, row)
  
  def _getCurrentCell(self) -> Cell:
    return self.maze.getCell(self.gridcoords())


  def _check(self):
    if (self.maze.isWall(self.gridcoords())):
      self._fail()

    self.maze.update()

  def _fail(self, undo=True):
    print("fail")
    if (_TRACER_N > 0):
      if (undo):
        self._turtle.undo()
      self._turtle.color("black","red")
      self.maze.pen.draw_failure()
      self._turtle.getscreen().mainloop()

  def _success(self):
    print("success")
    if (_TRACER_N > 0):
      self.maze.pen.draw_success()
      self._turtle.speed(8)
      self._turtle.right(360)
      self._turtle.left(360)
      self._turtle.getscreen().mainloop()

  def _process(self, cond):
    color = self._turtle.color()
    self._turtle.color("black", "orange")
    cell = self._getCurrentCell()
    if (cond(cell)):
      if (cell.value <= 0):
        self._fail()
      cell.value -= 1
      cell.redraw()
    else:
      self._fail()

    self._turtle.color(color[0], color[1])

  def _get_value_if(self, cellCond):
    cell = self._getCurrentCell()
    value = 0
    if (cellCond(cell)):
      value = cell.value
    return value
    
  def forward(self, steps=1):
    for i in range(steps):
      self._turtle.forward(50)
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
    cell = None
    if (head == Direction.NORTH.to_heading()):
      cell = self.maze.getCell((coords[0], coords[1]-1))
    elif (head == Direction.EAST.to_heading()):
      cell = self.maze.getCell((coords[0]+1, coords[1]))
    elif (head == Direction.SOUTH.to_heading()):
      cell = self.maze.getCell((coords[0], coords[1]+1))
    elif (head == Direction.WEST.to_heading()):
      cell = self.maze.getCell((coords[0]-1, coords[1]))
    
    return cell is not None and cell.isOpen()


# Get the directory of this Python file
_dir_path = os.path.dirname(os.path.realpath(__file__))

# Get the directory of the Python file being run
_script_path = os.path.dirname(os.path.realpath(sys.argv[0]))

def _search_path(filename, ext, failIfNotFound=True):
  if (not os.path.exists(filename)):
    filename = f"{filename}{ext}"
  
  # Typical scenario for the shape images
  othername = os.path.join(_dir_path, filename)
  if (os.path.exists(othername)):
    return othername
  

  
  if (not os.path.exists(filename)):
    filename = os.path.join("maze", filename)
  if (not os.path.exists(filename)):
    filename = os.path.join("src", filename)
  if (not os.path.exists(filename)):
    filename = os.path.join("maze", filename)
  if (not os.path.exists(filename)):
    filename = os.path.join("..", filename)
  if (not os.path.exists(filename)):
    if failIfNotFound:
      raise TypeError("Unable to shape file for " + filename)
  
  return filename

def _shapefile(name, ext=".gif"):
  return _search_path(name, ext)

