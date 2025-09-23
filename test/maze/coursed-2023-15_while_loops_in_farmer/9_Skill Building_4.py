from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while7_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/9



---
Fill in the hole at the end of each of these paths.
'''

# When run

for i in range(4):
    while farmer.path_ahead():
        farmer.forward()
    farmer.fill()
    farmer.left()

# Keep this
Puzzle.done()
