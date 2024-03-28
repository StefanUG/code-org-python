from enum import Enum
import turtle
import math
import random
import functools
import json
import os

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
    self.tileType = SquareType.list[tileType]
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


def enum(**enums):
    """
      Workaround to the fact that Trinket does not support proper Enums
    """
    return type('Enum', (), enums)


class _SquareType:
  value = None

  def __init__(self, value):
     self.value = value

  def isOpen(self):
    return self.value > 0
  
  def isWall(self):
    return self.value == 0

  def isStart(self):
    return self in [SquareType.START, SquareType.STARTANDFINISH]


SquareType = enum(
  WALL = _SquareType(0),
  OPEN = _SquareType(1),
  START = _SquareType(2),
  FINISH = _SquareType(3),
  OBSTACLE = _SquareType(4),
  STARTANDFINISH = _SquareType(5))

SquareType.list = [SquareType.WALL, SquareType.OPEN, SquareType.START, SquareType.FINISH, SquareType.OBSTACLE, SquareType.STARTANDFINISH]


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
HarvesterFeatureType = enum(NONE = 0, CORN = 1, PUMPKIN = 2, LETTUCE = 3)


###
### Bee Stuff
###
BeeFeatureType = enum(NONE = None, HIVE = 0, FLOWER = 1, VARIABLE = 2)
CloudType = enum(NONE = None, STATIC = 0, HIVE_OR_FLOWER = 1, FLOWER_OR_NOTHING = 2, HIVE_OR_NOTHING = 3, ANY = 4)
FlowerColor = enum(DEFAULT = None, RED = 0, PURPLE = 1)

class BeeCell(Cell):
  featureType = 0
  flowerColor = 0
  cloudType = 0  

  def __init__(self,tileType=0, value=0, range=0,featureType=None,flowerColor=None,cloudType=None):
    super().__init__(tileType=tileType, value=value, range=range)
    self.featureType = featureType
    self.flowerColor = flowerColor
    self.cloudType = cloudType

  def draw(self, x, y):
    super().draw(x, y)
    if (not self.isCloud() and self.featureType in (BeeFeatureType.NONE, BeeFeatureType.VARIABLE)):
      self.value = 0
    self.redraw()

  def isFlower(self):
    return self.featureType == BeeFeatureType.FLOWER

  def isHive(self):
    return self.featureType == BeeFeatureType.HIVE

  def redraw(self):
    if (self.isCloud() or self.featureType not in (BeeFeatureType.NONE, BeeFeatureType.VARIABLE)):
      self.showturtle()
    else:
      self.hideturtle()
    
    if (self.cloudType != CloudType.NONE):
      self.shape(_shapefile("cloud"))
    elif (self.isFlower()):
      if (self.flowerColor and self.flowerColor > 0):
        self.shape(_shapefile("purple_flower"))
      else:
        self.shape(_shapefile("red_flower"))
      self.drawValue()
    elif (self.isHive()):
      self.shape(_shapefile("honeycomb"))
      self.drawValue()

  def isCloud(self):
    return self.cloudType != CloudType.NONE
  
  def needs_visit(self):
    return self.isCloud() or self.isFlower() or self.isHive()
  
  def reveal(self):
    possibilities = None
    if (self.isCloud()):
      if (self.cloudType == CloudType.HIVE_OR_FLOWER):
        possibilities = [BeeFeatureType.HIVE, BeeFeatureType.FLOWER]
      elif (self.cloudType == CloudType.FLOWER_OR_NOTHING):
        possibilities = [BeeFeatureType.FLOWER, BeeFeatureType.FLOWER, BeeFeatureType.NONE]
      elif (self.cloudType == CloudType.HIVE_OR_NOTHING):
        possibilities = [BeeFeatureType.HIVE, BeeFeatureType.HIVE, BeeFeatureType.NONE]
      elif (self.cloudType == CloudType.ANY):
        possibilities = [BeeFeatureType.NONE, BeeFeatureType.HIVE, BeeFeatureType.FLOWER]

      if (possibilities):
        self.featureType = random.choice(possibilities)

      if (self.featureType == BeeFeatureType.NONE):
        # When there is no feature type, set the value to 0 so that 
        # we can detect the win condition properly
        self.value = 0
      elif self.value == 0:
        self.value = 1

      self.cloudType = CloudType.NONE
      self.redraw()



class Maze:
  @staticmethod
  def from_file(filename):
    if (not os.path.exists(filename)):
      filename = f"{filename}.json"
    if (not os.path.exists(filename)):
      filename = f"levels/{filename}"
    if (not os.path.exists(filename)):
      checklast = filename
      filename = f"../{filename}"
    if (not os.path.exists(filename)):
      filename = _search_path(checklast, "")

    if (not os.path.exists(filename)):
      raise TypeError("Unable to find file for level " + filename)
    
    with open(filename) as fp:
      level_json = json.load(fp)
      return Maze(level_json)

  @staticmethod
  def _testmode():
    global _TRACER_DELAY
    global _TRACER_N
    _TRACER_DELAY = 0
    _TRACER_N = 0


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

  def __init__(self, level):
    Maze.instance = self

    levelProps = level['properties']

    self.screen.bgcolor("white")
    self.screen.setup(410,410)
    self.screen.tracer(0,0)
    self.screen.bgpic(_shapefile(levelProps['skin'] + "_background", ".png"))

    # register sprites
    bee_shape = ((0,-22),(-4,-20),(-7,-13),(7,-13),(-7,-13),(-7.6,-5.6),(7.6,-5.6),(-7.6,-5.6),(-2.6,7.4),(-13.1,-10.5),(-18,-13),(-23,-11),(-25,-6),(-23,-1),(-2.6,7.5),(-7,9),(-6,15),(-4,17),(-7,20),(-11,22),(-7,20),(-4,17),(0,18),(4,17),(7,20),(11,22),(7,20),(4,17),(6,15),(7,9),(2.6,7.5),(23,-1),(25,-6),(23,-11),(18,-13),(13.1,-10.5),(2.6,7.4),(7.6,-5.6),(7,-13),(4,-20))

    self.screen.register_shape(_shapefile("cloud"))
    self.screen.register_shape(_shapefile("earth"))
    self.screen.register_shape(_shapefile("hole"))
    self.screen.register_shape(_shapefile("pile"))
    self.screen.register_shape(_shapefile("purple_flower"))
    self.screen.register_shape(_shapefile("red_flower"))
    self.screen.register_shape(_shapefile("honeycomb"))
    self.screen.register_shape("bee", bee_shape)

    if (levelProps['skin'] == 'bee'):
      self.cellType = BeeCell
      self.path = Path()

    self._setup_maze(level)

    self.pen.tick()
  

  def _setup_maze(self, level):
    levelProps = level['properties']
    parsed_maze = level.get('parsed_maze')
    if (not parsed_maze):
      parsed_maze = json.loads(levelProps["serialized_maze"])
      level['parsed_maze'] = parsed_maze

    maze = level['parsed_maze']
    startCell = None
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

  turtle = turtle.Turtle()

  def __init__(self, maze):
    Player.instance = self
    self.maze = maze

    self.turtle.color("black","yellow")
    self.turtle.shape("bee")
    self.turtle.penup()
    self.turtle.speed(1)

    self.at_hive = self.at_honeycomb

  def is_collision(self, other):
    a = self.turtle.xcor()-other.turtle.xcor()
    b = self.turtle.ycor()-other.turtle.ycor()
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
    col = round((self.maze.width/2  + (self.turtle.xcor()-25)) / 50)
    row = round((self.maze.height/2 - (self.turtle.ycor()+25) ) / 50)
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
        self.turtle.undo()
      self.turtle.color("black","red")
      self.maze.pen.draw_failure()
      self.turtle.getscreen().mainloop()

  def _success(self):
    print("success")
    if (_TRACER_N > 0):
      self.maze.pen.draw_success()
      self.turtle.speed(8)
      self.turtle.right(360)
      self.turtle.left(360)
      self.turtle.getscreen().mainloop()

  def _process(self, cond):
    color = self.turtle.color()
    self.turtle.color("black", "orange")
    cell = self._getCurrentCell()
    if (cond(cell)):
      cell.value -= 1
      cell.redraw()
    else:
      self._fail()

    self.turtle.color(color[0], color[1])

  def _get_value_if(self, cellCond):
    cell = self._getCurrentCell()
    value = 0
    if (cellCond(cell)):
      value = cell.value
    return value
    
  def forward(self, steps=1):
    for i in range(steps):
      self.turtle.forward(50)
      self._check()

  move_forward = forward
  go_forward = forward

  def right(self):
    self.turtle.right(90)

  def left(self):
    self.turtle.left(90)

  def at_flower(self):
    return self._getCurrentCell().isFlower()

  def at_honeycomb(self):
    return self._getCurrentCell().isHive()
  
  def nectar(self):
    return self._get_value_if(lambda cell: cell.isFlower())

  def honey(self):
    return self._get_value_if(lambda cell: cell.isHive())

  def path_ahead(self):
    coords = self.gridcoords()
    head = self.turtle.heading()
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

  def get_nectar(self):
    self._process(lambda cell: cell.isFlower())

  def make_honey(self):
    self._process(lambda cell: cell.isHive())



# Get the directory of the current Python file
_dir_path = os.path.dirname(os.path.realpath(__file__))

def _search_path(filename, ext):
  if (not os.path.exists(filename)):
    filename = f"{filename}{ext}"
  
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
    raise TypeError("Unable to shape file for " + filename)
  
  return filename

def _shapefile(name, ext=".gif"):
  return _search_path(name, ext)

