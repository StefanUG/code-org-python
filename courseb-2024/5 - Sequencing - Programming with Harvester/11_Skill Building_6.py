from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_seq9_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/5/levels/11

Add two blocks to finish this puzzle!

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
farmer.pick_corn()
farmer.east()
farmer.pick_corn()

# Keep this
Puzzle.done()