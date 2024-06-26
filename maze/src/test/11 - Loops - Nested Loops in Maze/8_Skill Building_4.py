from maze import Puzzle

maze = Puzzle.from_file("courseD_maze_nestedLoops5_2023")
zombie = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/8



---
Get the zombie to the sunflower using the fewest number of blocks possible!
'''

# When run

for i in range(2):
    zombie.forward(3)
    zombie.left()
    zombie.forward(3)
    zombie.right()
    

# Keep this
maze.done()