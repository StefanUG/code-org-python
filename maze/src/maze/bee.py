from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, _shapefile


class BeeMazeType(MazeType):
  
    def __init__(self):
        super().__init__(BeeCell, BeePlayer)

    def parse_cell_from_old_values(mapCell, initialDirtCell):
        mapCell = str(mapCell)
        initialDirtCell = int(initialDirtCell)
        tileType = featureType = value = cloudType = flowerColor = None

        if initialDirtCell != 0 and any(substring in mapCell for substring in ['1', 'R', 'P', 'FC']):
            tileType = SquareType.OPEN
            featureType = BeeFeatureType.FLOWER if initialDirtCell > 0 else BeeFeatureType.HIVE
            value = abs(initialDirtCell)
            cloudType = CloudType.STATIC if mapCell == 'FC' else CloudType.NONE
            if mapCell == 'R':
                flowerColor = FlowerColor.RED
            elif mapCell == 'P':
                flowerColor = FlowerColor.PURPLE
            else:
                flowerColor = FlowerColor.DEFAULT
        else:
            tileType = int(mapCell)

        return dict(tileType=tileType, featureType=featureType, value=value, cloudType=cloudType, flowerColor=flowerColor)



BEE_SHAPE = ((0,-22),(-4,-20),(-7,-13),(7,-13),(-7,-13),(-7.6,-5.6),(7.6,-5.6),(-7.6,-5.6),(-2.6,7.4),(-13.1,-10.5),(-18,-13),(-23,-11),(-25,-6),(-23,-1),(-2.6,7.5),(-7,9),(-6,15),(-4,17),(-7,20),(-11,22),(-7,20),(-4,17),(0,18),(4,17),(7,20),(11,22),(7,20),(4,17),(6,15),(7,9),(2.6,7.5),(23,-1),(25,-6),(23,-11),(18,-13),(13.1,-10.5),(2.6,7.4),(7.6,-5.6),(7,-13),(4,-20))

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
    self.cloudType   = CloudType(cloudType)

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
      if (self.flowerColor != FlowerColor.RED):
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


class BeePlayer(Player):

    def __init__(self, maze):
        super().__init__(maze)

        screen = self._turtle.getscreen()

        screen.register_shape("bee", BEE_SHAPE)

        self._turtle.color("black","yellow")
        self._turtle.shape("bee")


    def at_flower(self):
        return self._getCurrentCell().isFlower()

    def at_honeycomb(self):
        return self._getCurrentCell().isHive()
  
    def nectar(self):
        return self._get_value_if(lambda cell: cell.isFlower())

    def honey(self):
        return self._get_value_if(lambda cell: cell.isHive())

    def get_nectar(self):
        self._process(lambda cell: cell.isFlower())

    def make_honey(self):
        self._process(lambda cell: cell.isHive())
