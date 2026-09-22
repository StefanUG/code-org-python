from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_ramp13")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/2/levels/16



---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

# Start
for i in range(4):
    farmer.forward()
    farmer.pick_pumpkin()

# Keep this
Puzzle.done()