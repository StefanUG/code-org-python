from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_loops3_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/7/levels/4

Can you pick all the corn using only **one** move block?

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.pick_corn()
farmer.north() # limit: 1
farmer.south() # limit: 1
farmer.east() # limit: 1
farmer.west() # limit: 1
for i in range(4):
    # Do this
```
'''

# When run

# Start

# Keep this
Puzzle.done()