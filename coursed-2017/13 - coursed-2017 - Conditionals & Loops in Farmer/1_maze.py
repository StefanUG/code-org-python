from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops1")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/1

*"Corn you help me harvest today?"*

Help the harvester check her row of corn to see if anything is ready to pick.  Use conditionals to look at each sprout.  Every stalk will have either **0 or 1** pieces of corn ready to harvest.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
if farmer.has_corn():
    # Do this
farmer.pick_corn()
for i in range(5):
    # Do this
while farmer.path_ahead():
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()