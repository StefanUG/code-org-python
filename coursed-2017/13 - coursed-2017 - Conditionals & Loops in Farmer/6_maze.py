from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops6")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/6

*"Let's take this one step further!"*

Can you figure out how to pick the pumpkin?  Make sure to collect all of the corn along the way!

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.left()
while not farmer.at_pumpkin():
    # Do this
while farmer.has_corn():
    # Do this
if farmer.path_ahead():
    # Do this
if farmer.path_ahead():
    # Do this
else:
    # Otherwise this
farmer.pick_corn()
farmer.pick_pumpkin()
```
'''

# When run

# Start

# Keep this
Puzzle.done()