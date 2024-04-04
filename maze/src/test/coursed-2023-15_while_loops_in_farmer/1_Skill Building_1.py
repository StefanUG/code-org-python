from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while1_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/1

*"Hi, I'm a farmer. I need your help to flatten the field on my farm so it's ready for planting!"*  

Move to the pile of dirt and use the `remove` block to remove it.

---
Move to the pile of dirt and use the `remove` block to remove it.
'''

# When run

farmer.forward(4)
farmer.remove()

# Keep this
Puzzle.done()
