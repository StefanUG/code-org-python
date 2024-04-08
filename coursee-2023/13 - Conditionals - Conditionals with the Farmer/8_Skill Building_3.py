from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_ramp12b_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/13/levels/8

Now the harvester needs to pick all of the lettuce.  Use `while there is lettuce` inside of a `repeat` loop to get it all!

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
for i in range(5):
    # Do this
# 
```
'''

# When run

# Start

# Keep this
Puzzle.done()