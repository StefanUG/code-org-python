import os
import json

from .maze import Maze, Player, _script_path, _search_path
from .bee import BeePlayer

class Puzzle:
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
      filename = os.path.join(_script_path, checklast)
    if (not os.path.exists(filename)):
      filename = _search_path(checklast, "", False)

    if (not os.path.exists(filename)):
      raise TypeError("Unable to find file for level " + filename)
    
    with open(filename) as fp:
      level_json = json.load(fp)
      return Maze(level_json)