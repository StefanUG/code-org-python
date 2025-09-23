from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while8_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/10

**Challenge:** Fill all of these holes using as few blocks as possible. 

---
Challenge: Fill all of these holes using as few blocks as possible. 
'''

# When run

for i in range(6):
    while farmer.path_ahead():
        farmer.forward()
    while farmer.at_hole():
        farmer.fill()
    farmer.right()

# Keep this
Puzzle.done()
