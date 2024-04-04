from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while5_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/7



---
Help me remove all of this dirt. 
'''

# When run

for i in range(5):
    farmer.forward()
    while farmer.at_pile():
        farmer.remove()

# Keep this
Puzzle.done()
