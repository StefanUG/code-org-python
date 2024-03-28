from maze import *

maze = Maze.from_file("courseD_bee_nestedLoops1a_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/1

_"This is going to **BEE** great!"_

Help the bee collect all of the nectar.

---
Help the bee collect all of the nectar.
'''

# When run

bee.forward()
for i in range(2):
    bee.forward()
    bee.get_nectar()

# Keep this
done()