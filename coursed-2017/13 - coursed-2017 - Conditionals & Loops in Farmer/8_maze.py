from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops8")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/8

Collect all of the corn and lettuce, then pick the pumpkin.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
while not farmer.at_pumpkin():
    # Do this
while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this
farmer.pick_lettuce()
farmer.pick_pumpkin()
farmer.pick_corn()
if farmer.path_ahead():
    # Do this
else:
    # Otherwise this
if farmer.path_ahead():
    # Do this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
if farmer.has_lettuce():
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()