from maze import Puzzle

maze = Puzzle.from_file("courseD_maze_nestedLoops4_2023")
zombie = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/7

Get the zombie to the sunflower using the fewest blocks possible!  

---
Get the zombie to the sunflower using the fewest blocks possible!  
'''

# When run

for i in range(3):
    zombie.forward(3)
    zombie.right()

# Keep this
maze.done()