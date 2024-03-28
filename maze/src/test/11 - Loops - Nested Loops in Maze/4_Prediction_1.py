from maze import *

maze = Maze.from_file("courseD_bee_nestedLoops2_predict1_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/4

This time, help the bee collect all of the nectar using as few blocks as possible.

---
This time, help the bee collect all of the nectar using as few blocks as possible.
'''

# When run

for j in range(3):
    bee.forward()
    for i in range(2):
        bee.forward()
        bee.get_nectar()
    bee.right()

# Keep this
done()