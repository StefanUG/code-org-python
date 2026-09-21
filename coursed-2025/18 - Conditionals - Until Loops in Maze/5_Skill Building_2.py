from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_until4_2025")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/18/levels/5

*"Dear person. Me zombie. Me hungry. Must... get... to sunflower..."*

Can you get the zombie to the sunflower using only the blocks that are available?

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward()
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