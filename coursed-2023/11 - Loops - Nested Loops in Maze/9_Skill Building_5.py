from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_nestedLoops6_2023")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/9

*"Must eat sunflower!"*

Get the zombie to the sunflower using only the blocks available.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward()
zombie.left()
zombie.right()
for i in range(???):
    # Do this
# 
```
'''

# When run

# Start
zombie.forward()

# Keep this
Puzzle.done()