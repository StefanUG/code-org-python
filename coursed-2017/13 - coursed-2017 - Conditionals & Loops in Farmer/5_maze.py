from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops5")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/5

*"What a bountiful crop!"*

This field has clusters of corn and lettuce growing together -- with one pumpkin at the end.  Can you harvest everything?

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
while not farmer.at_pumpkin():
    # Do this
while farmer.path_ahead():
    # Do this
while farmer.has_corn():
    # Do this
farmer.pick_corn()
farmer.pick_pumpkin()
farmer.pick_lettuce()
if farmer.has_lettuce():
    # Do this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
```
'''

# When run



# Keep this
Puzzle.done()