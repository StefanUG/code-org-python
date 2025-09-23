from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops_challenge1a_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/14



---
Collect all of the corn.
'''

# When run

for i in range(2):
    farmer.forward()
    farmer.pick_corn()
farmer.right()
for i in range(2):
    for j in range(4):
        farmer.forward()
        farmer.pick_corn()
    farmer.right()
for i in range(6):
    farmer.forward()
    farmer.pick_corn()

# Keep this
Puzzle.done()
