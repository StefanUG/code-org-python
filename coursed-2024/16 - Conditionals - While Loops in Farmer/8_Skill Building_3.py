from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while6_2024")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/16/levels/8

Look at all of those holes!  Each one needs a different amount of dirt.   

You can use the `while` loop to easily fill them all!

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.remove()
farmer.fill()
for i in range(5): # limit: 1
    # Do this
while farmer.at_hole():
    # Do this
# 
```
'''

# When run

# Start

# Keep this
Puzzle.done()