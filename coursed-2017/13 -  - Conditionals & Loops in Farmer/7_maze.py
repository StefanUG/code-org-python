from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops7")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/7

**Challenge:** Collect all of the corn and lettuce, then pick the pumpkin.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
if farmer.has_lettuce():
    # Do this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
farmer.pick_pumpkin()
farmer.pick_corn()
farmer.pick_lettuce()
while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this
while not farmer.at_pumpkin():
    # Do this
for i in range(6): # limit: 1
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()