from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_conditionals10_2023")
bee = maze.player

'''
Conditionals can be helpful, even when you know exactly what is in each spot!

Collect all of the nectar and make all of the honey.


Collect all of the nectar and make all of the honey.
'''

# When run

for i in range(7):
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()


# Keep this
maze.done()