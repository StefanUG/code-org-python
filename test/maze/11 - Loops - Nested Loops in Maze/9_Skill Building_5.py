from maze import Puzzle

maze = Puzzle.from_file("courseD_maze_nestedLoops6_2023")
zombie = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/9

*"Must eat sunflower!"*

Get the zombie to the sunflower using only the blocks available.

---
Get the zombie to the sunflower using only the blocks available.
'''

# When run

for i in range(3):
    zombie.forward(5)
    zombie.left()

for i in range(2):
    zombie.forward(3)
    zombie.left()

# Keep this
Puzzle.done()