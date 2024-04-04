from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while10_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/12



---
Flatten all of these piles using as few blocks as possible. 
'''

# When run

for i in range(3):
    while farmer.path_ahead():
        farmer.forward()
    while farmer.at_pile():
        farmer.remove()
    farmer.left()
    while farmer.path_ahead():
        farmer.forward()
    farmer.right()

# Keep this
Puzzle.done()
