import turtle
import math
from enum import Enum

maze_instance = None
pegman_instance = None

def forward(steps=1):
  pegman_instance.go_forward(steps)

def right():
  pegman_instance.right()

def left():
  pegman_instance.left()

def atFlower():
  pegman_instance


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
    self.shape("earth.gif")
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

    self.penup()
    self.speed(0)

    self.hideturtle()
      

  def draw(self, x, y):
    self.x = x
    self.y = y

    self.goto(x, y)


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


###
### Harvester Stuff
###

class HarvesterFeatureType(Enum):
  NONE = 0
  CORN = 1
  PUMPKIN = 2
  LETTUCE = 3


###
### Bee Stuff
###

class BeeFeatureType(Enum):
  NONE = None
  HIVE = 0
  FLOWER = 1
  VARIABLE = 2

class CloudType(Enum):
  NONE = None
  STATIC = 0
  HIVE_OR_FLOWER = 1
  FLOWER_OR_NOTHING = 2
  HIVE_OR_NOTHING = 3
  ANY = 4

class FlowerColor(Enum):
  DEFAULT = None
  RED = 0
  PURPLE = 1

class BeeCell(Cell):
  featureType = 0
  flowerColor = 0
  cloudType = 0  

  def __init__(self,tileType=0, value=0, range=0,featureType=None,flowerColor=None,cloudType=None):
    super().__init__(tileType=tileType, value=value, range=range)
    self.featureType = BeeFeatureType(featureType)
    self.flowerColor = FlowerColor(flowerColor)
    self.cloudType = CloudType(cloudType)

  def draw(self, col, row):
    super().draw(col, row)

    if (self.featureType != BeeFeatureType.NONE):
      self.showturtle()
    
    if (self.cloudType != CloudType.NONE):
      self.shape("cloud.gif")
    elif (self.featureType == BeeFeatureType.FLOWER):
      if (self.flowerColor > 0):
        self.shape("purple_flower.gif")
      else:
        self.shape("red_flower.gif")

    
    




class Maze:
  screen = turtle.Screen()
  treasures = []
  walls = []
  player = None
  path = None

  width = 0
  height = 0
  
  currentStaticGrid = None
  cellType = Cell

  grid = []

  def __init__(self, level):
    self.screen.bgcolor("white")
    self.screen.setup(410,410)
    self.screen.tracer(0)
    self.screen.bgpic(f"{level['skin']}_background.png")

    # register sprites
    bee_shape = ((0,-22),(-4,-20),(-7,-13),(-7.6,-5.6),(-2.6,7.4),(-13.1,-10.5),(-18,-13),(-23,-11),(-25,-6),(-23,-1),(-2.6,7.5),(-7,9),(-6,15),(-4,17),(-7,20),(-11,22),(-7,20),(-4,17),(0,18),(4,17),(7,20),(11,22),(7,20),(4,17),(6,15),(7,9),(2.6,7.5),(23,-1),(25,-6),(23,-11),(18,-13),(13.1,-10.5),(2.6,7.4),(7.6,-5.6),(7,-13),(4,-20))

    self.screen.register_shape("cloud.gif")
    self.screen.register_shape("earth.gif")
    self.screen.register_shape("hole.gif")
    self.screen.register_shape("pile.gif")
    self.screen.register_shape("purple_flower.gif")
    self.screen.register_shape("red_flower.gif")
    self.screen.register_shape("bee", bee_shape)

    if (level['skin'] == 'bee'):
      self.cellType = BeeCell
      self.path = Path()

    self.currentStaticGrid = level

    self.setup_maze(level["serialized_maze"])
    global pegman_instance
    pegman_instance = self.player

    self.screen.tracer(1,10)


  def setup_maze(self, level):
    startCell = None
    rows = len(level)
    self.height = rows * 50
    self.grid = []
    
    for y in range(rows):
      row = []
      self.grid.append(row)
      cols = len(level[y])
      for x in range(cols):
        if (self.width == 0):
          self.width = cols * 50

        cell = self.cellType(**level[y][x])
        row.append(cell)

        screen_x = -1*((self.width/2)-25) + (x * 50)
        screen_y = (self.height/2-25) - (y * 50)

        if (self.path and cell.tileType.isOpen()):
          self.path.draw(screen_x, screen_y)
        
        cell.draw(screen_x, screen_y)

        if (cell.tileType == SquareType.WALL):
          self.walls.append((x, y))

        if (cell.tileType.isStart()):
          startCell = cell

    self.player = Player(self)
    self.player.turtle.goto(startCell.x, startCell.y)


  def getCell(self, gridcoords):
    return self.grid[gridcoords[1]][gridcoords[0]]

  def isWall(self, gridcoords):
    cell = self.getCell(gridcoords)
    return cell.tileType.isWall()



  def update(self):
    for treasure in treasures:
      if player.is_collision(treasure):
        player.gold += treasure.gold
        game["gold_left"] -= 1
        print(game["gold_left"])
        treasure.destroy()
        game["treasures"].remove(treasure)
        if player.gold == 100:
          print("lt 100")
        else:
          turtle.clear()
          turtle.goto(-50,300)
          turtle.write("Player Gold:{}".format(player.gold),align="right",font=(0.0000001))
          turtle.goto(2000,2000)
          self.update()



class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v=self.getscreen()
        v.register_shape("./image/treasure.gif")
        self.shape("./image/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Player():
  maze:Maze = None

  turtle = turtle.Turtle()

  def __init__(self, maze: Maze ):
    self.maze = maze

    self.turtle.color("yellow")
    self.turtle.shape("bee")
    self.turtle.penup()
    self.turtle.speed(1)

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
  
  def getCurrentCell(self):
    return self.maze.getCell(self.gridcoords())


  def check(self):
    if (self.maze.isWall(self.gridcoords())):
      self.fail()
    



  def fail(self):
    self.turtle.undo()
    self.turtle.color("red")
    self.turtle.getscreen().mainloop()

  def go_forward(self, steps):
    self.turtle.forward(steps * 50)
    self.check()

  def right(self):
    self.turtle.right(90)
    self.check()

  def left(self):
    self.turtle.left(90)
    self.check()