from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_seq7_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/5/levels/9

You have to move in two directions to get to the corn! Help the harvester pick the right direction.

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
farmer.east()
farmer.east()
farmer.north()
farmer.pick_corn()

# Keep this
Puzzle.done()