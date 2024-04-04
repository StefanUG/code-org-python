from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops8_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/9

**Challenge:** Collect all of the corn and all of the pumpkins.

You can complete this challenge any way you want, but it will either take a lot of work or a lot of thinking!

---
**Challenge:** Collect all of the corn and all of the pumpkins.
'''

# When run

for i in range(7):
    farmer.forward()
    for j in range(4):
        farmer.pick_corn()
    farmer.right()
    farmer.forward()
    for j in range(6):
        farmer.pick_pumpkin()
    farmer.left()


# Keep this
Puzzle.done()
