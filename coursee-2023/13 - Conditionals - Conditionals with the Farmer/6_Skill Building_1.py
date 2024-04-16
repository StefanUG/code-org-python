from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseE_farmer_ramp11a_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/13/levels/6

Oh my!  This pile is so big that it's hard to guess how much dirt is in it.  

___

We've added a new block to the toolbox called the `while there is a pile` block.  Use this to remove dirt only while there is still some to scoop! 

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.remove() # limit: 1
while farmer.at_pile():
    # Do this
# 
```
'''

# When run

# Start

# Keep this
Puzzle.done()