from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops2")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/2

*"Lettuce collect both crops from this row!"*

This garden is all mixed up, it has both **corn and lettuce**!  

Help the harvester pick the items that are ready for harvesting.  Each plant will have either **one** corn or **one** lettuce.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
if farmer.has_lettuce():
    # Do this
farmer.pick_corn()
farmer.pick_lettuce()
for i in range(5):
    # Do this
while farmer.path_ahead():
    # Do this
```
'''

# When run

# Start

# Keep this
Puzzle.done()