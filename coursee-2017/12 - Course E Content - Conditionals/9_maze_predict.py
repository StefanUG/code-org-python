from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_predict2")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/12/levels/9



---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

# Start
while not farmer.has_pumpkin():
    farmer.forward()
farmer.pick_pumpkin()

# Keep this
Puzzle.done()