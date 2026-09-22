from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops_challenge2")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/12

*"It's a very varied vegetable maze!"* 

Turn right at pumpkins, turn left at lettuce. Collect everything to complete the level.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward() # limit: 1
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
for i in range(6):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()