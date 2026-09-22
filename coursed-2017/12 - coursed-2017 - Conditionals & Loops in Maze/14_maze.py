from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_until_challenge1")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/12/levels/14

No hints, just challenge. Get the zombie to the sunflower.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 1
zombie.right()
zombie.left()
if zombie.path_ahead(): # limit: 2
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