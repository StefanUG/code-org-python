from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_seq5_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/5/levels/7

Can you figure out what is wrong with this code? Help the harvester pick the corn!

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
farmer.west()
farmer.north()
farmer.west()
farmer.pick_corn()

# Keep this
Puzzle.done()