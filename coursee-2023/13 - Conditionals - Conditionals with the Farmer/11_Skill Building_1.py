from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseE_farmer_ramp12c_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/13/levels/11

The lettuce is now only at the end of the path.  
Travel down the path **until** you reach a head of lettuce, then continue to pick it **while** there is still some left.  

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
# 
```
'''

# When run

# Start

# Keep this
Puzzle.done()