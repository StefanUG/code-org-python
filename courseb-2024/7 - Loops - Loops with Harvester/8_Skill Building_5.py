from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_loops5b_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/7/levels/8

Can you change your code to make the harvester pick all the corn?

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.pick_corn()
farmer.north() # limit: 1
farmer.south() # limit: 1
farmer.east() # limit: 1
farmer.west() # limit: 1
for i in range(6):
    # Do this
```
'''

# When run

# Start
for i in range(6):
    farmer.south()
    farmer.pick_corn()
for i in range(6):
    farmer.east()
    farmer.pick_corn()

# Keep this
Puzzle.done()