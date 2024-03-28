from maze import *

maze = Maze.from_file("courseD_bee_nestedLoops9_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/12

Make all of the honey.

![]()

---
Make all of the honey.
'''

# When run

for i in range(2):
    for j in range(5):
        bee.forward()
        bee.make_honey()
    bee.left()


# Keep this
done()