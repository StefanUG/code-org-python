from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while2_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/2



---
Move to the hole and fill it with six shovelfuls of dirt, using the `fill` block.
'''

# When run

farmer.forward()
for i in range(6):
    farmer.fill()

# Keep this
Puzzle.done()
