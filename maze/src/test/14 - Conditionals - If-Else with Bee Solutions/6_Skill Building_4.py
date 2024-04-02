from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_conditionals5_2023")
bee = maze.player

'''



Collect all of the nectar using as few blocks as possible
'''

# When run

for i in range(2):
    for j in range(6):
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()
    bee.left()
    bee.forward()
    bee.forward()
    bee.left()

# Keep this
maze.done()