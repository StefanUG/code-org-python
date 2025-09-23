from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseC_harvester_loops2_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/9/levels/3

Can you combine two different loops to move toward the pumpkins, then collect them all?

---
Can you combine two different loops to move toward the pumpkins, then collect them all?
'''

# When run

farmer.forward(5)
for i in range(4):
    farmer.pick_pumpkin()

# Keep this
Puzzle.done()
