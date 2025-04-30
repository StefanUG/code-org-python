from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while6_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/8

Look at all of those holes!  Each one needs a different amount of dirt.   

You can use the `while` loop to easily fill them all!

---
Use the `while` loop to easily fill all of the holes.
'''

# When run

for i in range(3):
    farmer.forward()
    while farmer.at_hole():
        farmer.fill()
    farmer.right()
    farmer.forward()
    while farmer.at_hole():
        farmer.fill()
    farmer.left()

# Keep this
Puzzle.done()
