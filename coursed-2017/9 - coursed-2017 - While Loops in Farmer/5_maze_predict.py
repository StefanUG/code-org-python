from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while4_predict1")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/9/levels/5

*"I don't know how much dirt is in this pile!"*

Help the farmer remove this entire pile using a `while` loop.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.remove()
farmer.fill()
for i in range(5):
    # Do this
while farmer.at_pile():
    # Do this
```
'''

# When run

# Start
farmer.forward()
while farmer.at_pile():
    farmer.remove()

# Keep this
Puzzle.done()