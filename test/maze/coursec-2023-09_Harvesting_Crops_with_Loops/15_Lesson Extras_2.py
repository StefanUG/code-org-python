from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops_challenge2_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/15

Collect all of the lettuce. Avoid the trees and fields!

---
Collect all of the lettuce. Avoid the trees and fields!
'''

# When run

for i in range(3):
    for j in range(3):
        farmer.forward(2)
        farmer.pick_lettuce()
    farmer.right()

for i in range(2):
    for j in range(2):
        farmer.forward(2)
        farmer.pick_lettuce()
    farmer.right()

for i in range(2):
    farmer.forward(2)
    farmer.pick_lettuce()
    farmer.right()

# Keep this
Puzzle.done()
