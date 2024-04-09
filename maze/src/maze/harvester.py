from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze
from .farmer import Farmer


class HarvesterFeatureType(Enum):
    NONE = 0
    CORN = 1
    PUMPKIN = 2
    LETTUCE = 3


class HarvesterMazeType(MazeType):

    def __init__(self):
        super().__init__()
        self.cellClass = HarvesterCell
        self.playerClass = Harvester
        self.subfolder = "farmer"

    def setup(self, level, screen):
        super().setup(level, screen)
        screen.bgpic(Maze.shapefile("background", ".png"))
        screen.register_shape(Maze.shapefile("path"))
        screen.register_shape(Maze.shapefile("sprout"))
        screen.register_shape(Maze.shapefile("lettuce"))
        screen.register_shape(Maze.shapefile("corn"))
        screen.register_shape(Maze.shapefile("pumpkin"))

    def success(self, maze, player):
        self.path().clear()
        super().success(maze, player)


class HarvesterCell(Cell):

    def __init__(self, tileType=0, value=0, range=0, featureType=0, possibleFeatures: list = None, startsHidden=False):
        super().__init__(tileType=tileType, value=value, range=range)

        self.feature_type = HarvesterFeatureType(featureType)

        if type(possibleFeatures) is list:
            self.possible_features = list(map(lambda feature: HarvesterFeatureType(feature), possibleFeatures))
        else:
            self.possible_features = [HarvesterFeatureType.NONE]

        self.feature_type = random.choice(self.possible_features)
        if self.feature_type == HarvesterFeatureType.NONE:
            self.value = 0

        if len(self.possible_features) > 1:
            startsHidden = True

        self.starts_hidden = startsHidden

    def redraw(self):
        if self.starts_hidden:
            self.shape(Maze.shapefile("sprout"))
            self.showturtle()
        elif self.is_crop() and self.value > 0:
            self.shape(Maze.shapefile(self.feature_type.name.lower()))
            self.showturtle()
        else:
            self.hideturtle()

        if self.value != 0 and not self.starts_hidden:
            self.draw_value()

        if self.originalValue != 0 and self.value == 0:
            # Clear any value that might have been previously written
            self.clear()

    def reveal(self):
        if self.starts_hidden:
            self.starts_hidden = False
            self.redraw()

    def is_corn(self):
        return self.feature_type == HarvesterFeatureType.CORN

    def is_lettuce(self):
        return self.feature_type == HarvesterFeatureType.LETTUCE

    def is_pumpkin(self):
        return self.feature_type == HarvesterFeatureType.PUMPKIN

    def is_crop(self):
        return self.feature_type is not HarvesterFeatureType.NONE

    def needs_visit(self):
        return self.originalValue != 0


class Harvester(Farmer):

    def __init__(self, maze):
        super().__init__(maze)

    def pick_pumpkin(self):
        """
        Pick a pumpkin ripe for the taking
        :return:
        """
        self._process(lambda cell: cell.is_pumpkin())

    def pick_corn(self):
        """
        Pick the corn
        :return:
        """
        self._process(lambda cell: cell.is_corn())

    def pick_lettuce(self):
        """
        Pick the corn
        :return:
        """
        self._process(lambda cell: cell.is_lettuce())

    def at_corn(self):
        return self._get_current_cell().is_corn()

    def at_pumpkin(self):
        return self._get_current_cell().is_pumpkin()

    def at_lettuce(self):
        return self._get_current_cell().is_lettuce()

    def has_corn(self):
        cell: FarmerCell = self._get_current_cell()
        return cell.is_corn() and cell.value > 0

    def has_pumpkin(self):
        cell: FarmerCell = self._get_current_cell()
        return cell.is_pumpkin() and cell.value > 0

    def has_lettuce(self):
        cell: FarmerCell = self._get_current_cell()
        return cell.is_lettuce() and cell.value > 0
