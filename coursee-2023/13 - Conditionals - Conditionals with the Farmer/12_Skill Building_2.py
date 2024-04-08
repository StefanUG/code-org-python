from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_ramp12d_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/13/levels/12

The lettuce is scattered all over the garden.  
Travel down each path **until** you reach a head of lettuce, then continue to pick it **while** there is still some left.  

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.pick_lettuce()
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