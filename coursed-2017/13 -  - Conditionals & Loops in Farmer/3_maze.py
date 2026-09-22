from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops3")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/3

*"Corn, lettuce, AND pumpkins! Help me harvest them all."*

Each plant will have either one piece of corn, one head of lettuce, or one pumpkin.

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
if farmer.has_pumpkin():
    # Do this
farmer.pick_corn()
farmer.pick_pumpkin()
farmer.pick_lettuce()
for i in range(5):
    # Do this
while farmer.path_ahead():
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()