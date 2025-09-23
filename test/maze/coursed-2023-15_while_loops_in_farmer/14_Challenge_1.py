from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while_challenge1_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/14

Fill all of the holes and remove all of the piles.

---
Fill all of the holes and remove all of the piles.
'''

# When run

while farmer.path_ahead():
    while farmer.path_ahead():
        farmer.forward()
    farmer.backward()
    while farmer.at_pile():
        farmer.remove()
    while farmer.at_hole():
        farmer.fill()
    farmer.right()


# Keep this
Puzzle.done()
