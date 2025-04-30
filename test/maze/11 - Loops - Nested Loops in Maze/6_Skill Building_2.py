from maze import Puzzle

maze = Puzzle.from_file("courseD_maze_nestedLoops3_2023")
zombie = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/6

*"Zombie hungry!"*

Get the zombie to the sunflower using the fewest number of blocks possible.

---
Get the zombie to the sunflower using the fewest number of blocks possible.
'''

# When run

for i in range(3):
    zombie.forward(3)
    zombie.left()


# Keep this
maze.done()