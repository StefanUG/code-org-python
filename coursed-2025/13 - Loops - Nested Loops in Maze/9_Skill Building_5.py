from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_nestedLoops6_2025")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/13/levels/9

*"Must eat sunflower!"*

Get the zombie to the sunflower using only the blocks available.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 2
zombie.left()
zombie.right()
for i in range(???): # limit: 4
    # Do this
# 
```
'''

# When run

# Start
zombie.forward()

# Keep this
Puzzle.done()