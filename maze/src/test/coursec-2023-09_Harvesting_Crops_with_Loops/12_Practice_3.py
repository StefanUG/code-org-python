from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops11_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/12

Collect all of the corn and all of the pumpkins.

---
Collect all of the corn and all of the pumpkins.
'''

# When run

for i in range(4):
    farmer.forward()
    farmer.pick_corn()
    farmer.left()
    farmer.forward()
    farmer.pick_pumpkin()
    farmer.right()

# Keep this
Puzzle.done()
