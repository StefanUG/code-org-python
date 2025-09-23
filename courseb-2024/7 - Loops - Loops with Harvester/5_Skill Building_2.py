from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_loops4_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/7/levels/5

*"I need help to find what's wrong!"*

Can you help the harvester find the bug in her code?

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
for i in range(4):
    farmer.south()
    farmer.pick_corn()

# Keep this
Puzzle.done()