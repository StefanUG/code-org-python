from maze import *

maze = Maze.from_file("courseD_bee_nestedLoops7_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/10

**Challenge:** Figure out how to get all of the nectar using only the blocks available.

---
Challenge: Figure out how to get all of the nectar using only the blocks available.
'''

# When run

for j in range(4):
    for i in range(3):
        for n in range(12):
            bee.get_nectar()
        bee.forward()
    bee.right()


# Keep this
done()