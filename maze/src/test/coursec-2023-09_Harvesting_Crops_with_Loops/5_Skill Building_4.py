from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops4_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/5

Now there is corn growing, too!

Collect all of the corn and all of the pumpkins.

---
Collect all of the corn and all of the pumpkins.
'''

# When run

farmer.forward(2)
for i in range(6):
    farmer.pick_corn()
farmer.forward()
for i in range(4):
    farmer.pick_pumpkin()
farmer.forward(2)
for i in range(6):
    farmer.pick_corn()
farmer.forward()
for i in range(4):
    farmer.pick_pumpkin()


# Keep this
Puzzle.done()
