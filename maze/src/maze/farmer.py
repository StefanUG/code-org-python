from enum import Enum
import random
from .maze import SquareType, MazeType, Cell, Player, Maze

FARMER_SHAPE = (
    (0, -15), (-5, -13), (-9, -8), (-9, 0), (-7, 5), (-9, 0), (-9, -8), (-5, -13), (-15, -12), (-19, -9), (-19, 0),
    (-16, 9), (-7, 5), (-16, 9), (-15, 13), (-9, 13), (-7, 11), (-7, 5), (0, 8), (7, 5), (7, 11), (9, 13), (15, 13),
    (16, 9), (7, 5), (16, 9), (19, 0), (19, -9), (15, -12), (5, -13), (9, -8), (9, 0), (7, 5), (9, 0), (9, -8),
    (5, -13), (0, -15))


class HarvesterFeatureType(Enum):
    NONE = 0
    CORN = 1
    PUMPKIN = 2
    LETTUCE = 3


class FarmerMazeType(MazeType):

    def __init__(self, skin):
        super().__init__()
        self.skin = skin
        self.cellClass = FarmerCell
        self.playerClass = Farmer
        self.subfolder = "farmer"

    def setup(self, level, screen):
        super().setup(level, screen)
        FarmerCell.skin = self.skin
        screen.bgpic(Maze.shapefile("background", ".png"))
        screen.register_shape(Maze.shapefile("path"))
        screen.register_shape(Maze.shapefile("sprout"))
        screen.register_shape(Maze.shapefile("lettuce"))
        screen.register_shape(Maze.shapefile("corn"))
        screen.register_shape(Maze.shapefile("pumpkin"))
        screen.register_shape(Maze.shapefile("hole"))
        screen.register_shape(Maze.shapefile("pile"))

    def success(self, maze, player):
        self.path().clear()
        super().success(maze, player)


class FarmerCell(Cell):

    skin = None

    def __init__(self, tileType=0, value=0, range=0, featureType=0, possibleFeatures: list = None, startsHidden=False):
        super().__init__(tileType=tileType, value=value, range=range)

        if FarmerCell.skin == "farmer":
            # The harvester feature types do not apply to the farmer
            self.feature_type = HarvesterFeatureType.NONE
            self.starts_hidden = False
            return

        self.feature_type = HarvesterFeatureType(featureType)

        if type(possibleFeatures) is list:
            self.possible_features = list(map(lambda feature: HarvesterFeatureType(feature), possibleFeatures))
        else:
            self.possible_features = [HarvesterFeatureType.NONE]

        self.feature_type = random.choice(self.possible_features)

        if len(self.possible_features) > 1:
            startsHidden = True

        self.starts_hidden = startsHidden

    def draw(self, x, y):
        super().draw(x, y)
        self.redraw()

    def redraw(self):
        if self.is_crop() and self.value > 0:
            if self.starts_hidden:
                self.shape(Maze.shapefile("sprout"))
            else:
                self.shape(Maze.shapefile(self.feature_type.name.lower()))
            self.showturtle()
        elif self.value != 0:
            if self.is_hole():
                self.shape(Maze.shapefile("hole"))
            else:
                self.shape(Maze.shapefile("pile"))
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

    def is_hole(self):
        return not self.is_crop() and self.value < 0

    def is_pile(self):
        return not self.is_crop() and self.value > 0

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

    def at_pile(self):
        return self._get_current_cell().is_pile()

    def at_hole(self):
        return self._get_current_cell().is_hole()

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
