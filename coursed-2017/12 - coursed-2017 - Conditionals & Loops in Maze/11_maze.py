from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_until9")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/12/levels/11

**Challenge:** Avoid the chompers and help the zombie get to the sunflower.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 1
zombie.right()
zombie.left()
if zombie.path_ahead():
    # Do this
else:
    # Otherwise this
if zombie.path_ahead():
    # Do this
while not zombie.at_finish():
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()