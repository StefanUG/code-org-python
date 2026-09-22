from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops9_predict1")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/10

Collect all of the corn and lettuce, then pick the pumpkin.

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
for i in range(6): # limit: 1
    # Do this
```
'''

# When run

# Start
while not farmer.has_pumpkin():
    farmer.forward()
    farmer.left()
    farmer.forward()
    farmer.right()
    while farmer.has_corn():
        farmer.pick_corn()
    while farmer.has_lettuce():
        farmer.pick_lettuce()

# Keep this
Puzzle.done()