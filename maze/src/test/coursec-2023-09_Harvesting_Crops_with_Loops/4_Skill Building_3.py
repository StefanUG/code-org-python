from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops3_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/4

Collect all of the pumpkins.

---
Collect all of the pumpkins.
'''

# When run

farmer.forward(5)
for i in range(4):
    farmer.pick_pumpkin()
farmer.right()
farmer.forward(5)
for i in range(4):
    farmer.pick_pumpkin()
farmer.right()
farmer.forward(5)
for i in range(4):
    farmer.pick_pumpkin()
farmer.right()


# Keep this
Puzzle.done()
