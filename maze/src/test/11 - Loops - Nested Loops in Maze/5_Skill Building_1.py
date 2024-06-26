from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_nestedLoops2_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/5

This time, help the bee collect all of the nectar using as few blocks as possible.

---
This time, help the bee collect all of the nectar using as few blocks as possible.
'''

# When run

for j in range(4):
    for i in range(3):
        bee.get_nectar()
        bee.forward()
    bee.right()


# Keep this
maze.done()