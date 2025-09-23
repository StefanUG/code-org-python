from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_until5_2024")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/17/levels/6

Use the `if` block to help the zombie decide when to turn, then get the zombie to the sunflower.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 1
zombie.right()
zombie.left()
while zombie.path_ahead():
    # Do this
while not zombie.at_finish():
    # Do this
if zombie.path_left():
    # Do this
# 
```
'''

# When run



# Keep this
Puzzle.done()