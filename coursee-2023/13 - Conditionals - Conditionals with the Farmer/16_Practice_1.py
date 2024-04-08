from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_while1_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/13/levels/16

Move forward until you get to the lettuce, then turn left **if** there is a path to the left.  Otherwise, turn right.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.pick_lettuce()
if farmer.path_left():
    # Do this
else:
    # Otherwise this
while farmer.has_lettuce():
    # Do this
while not farmer.has_lettuce():
    # Do this
for i in range(5):
    # Do this
# 
```
'''

# When run

# Start

# Keep this
Puzzle.done()