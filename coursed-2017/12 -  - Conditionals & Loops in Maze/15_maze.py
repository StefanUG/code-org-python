from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_until_challenge2")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/12/levels/15

Use `If/Else` blocks to follow the curvy path. At each corner, use the `remove 1` block in a loop to clear the piles.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.backward()
farmer.left()
farmer.right()
farmer.remove()
farmer.fill()
for i in range(5):
    # Do this
while farmer.path_ahead(): # limit: 3
    # Do this
if farmer.path_ahead(): # limit: 2
    # Do this
else:
    # Otherwise this
```
'''

# When run

# Start

# Keep this
Puzzle.done()