from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_seq3_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/5/levels/4

Use **three** <xml><block type="maze_moveNorth" block-text="move north"/></xml> blocks to get the harvester to the corn! Don't forget to pick the corn at the end.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.pick_corn()
farmer.north()
farmer.south()
farmer.east()
farmer.west()
for i in range(3):
    # Do this
```
'''

# When run

# Start

# Keep this
Puzzle.done()