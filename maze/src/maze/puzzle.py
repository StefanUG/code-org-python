import os
import sys
import json

from .maze import Maze, Player
from .bee import BeeMazeType
from .pvz import ZombieMazeType
from .farmer import FarmerMazeType

# Get the directory of the Python file being run
_script_path = os.path.dirname(os.path.realpath(sys.argv[0]))


def _search_path(filename, ext, failIfNotFound=True):
    if not os.path.exists(filename):
        filename = f"{filename}{ext}"
    if not os.path.exists(filename):
        filename = os.path.join("maze", filename)
    if not os.path.exists(filename):
        filename = os.path.join("src", filename)
    if not os.path.exists(filename):
        filename = os.path.join("maze", filename)
    if not os.path.exists(filename):
        filename = os.path.join("..", filename)
    if not os.path.exists(filename):
        if failIfNotFound:
            raise TypeError("Unable to shape file for " + filename)

    return filename


class Puzzle:
    mazeTypes = {
        "bee": BeeMazeType(),
        "pvz": ZombieMazeType(),
        "farmer": FarmerMazeType(),
        "harvester": FarmerMazeType()
    }

    @staticmethod
    def from_file(filename):
        if not os.path.exists(filename):
            filename = f"{filename}.json"
        if not os.path.exists(filename):
            filename = f"levels/{filename}"
        if not os.path.exists(filename):
            checklast = filename
            filename = f"../{filename}"
        if not os.path.exists(filename):
            filename = os.path.join(_script_path, checklast)
        if not os.path.exists(filename):
            filename = _search_path(checklast, "", False)

        if not os.path.exists(filename):
            raise TypeError("Unable to find file for level " + filename)

        with open(filename) as fp:
            level_json = json.load(fp)

            game_id = level_json.get("game_id")
            if game_id and int(game_id) == 25:
                levelProps = level_json['properties']

                mazeType = Puzzle.mazeTypes[levelProps["skin"]]

                return Maze(level_json, mazeType)
            else:
                print(f"Unknown game_id: {game_id}")

    @staticmethod
    def done():
        Maze.instance.done()
