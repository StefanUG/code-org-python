from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while_challenge1_2024")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/16/levels/14

Fill all of the holes and remove all of the piles.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward() # limit: 2
farmer.backward() # limit: 2
farmer.right()
farmer.left()
farmer.remove() # limit: 1
farmer.fill() # limit: 1
for i in range(5):
    # Do this
while farmer.path_ahead():
    # Do this
while farmer.at_hole():
    # Do this
```
'''

# When run

# Start

# Keep this
Puzzle.done()