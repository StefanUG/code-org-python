from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops7_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/7

Collect all of the corn and all of the pumpkins.

---
Collect all of the corn and all of the pumpkins.
'''

# When run

for i in range(5):
    farmer.forward()
    farmer.pick_corn()
farmer.right()
farmer.forward()
farmer.right()
for i in range(5):
    farmer.forward()
for i in range(7):
    farmer.pick_pumpkin()


# Keep this
Puzzle.done()
