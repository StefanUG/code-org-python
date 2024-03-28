from maze import *

maze = Maze.from_file("courseD_bee_conditionals8_2023")
bee = maze.player

'''
**Challenge:** There will be either a flower or a honeycomb under each of those clouds!

Collect nectar once if there is a flower.
Otherwise, make honey once (because there is a honeycomb).


Collect nectar if there is a flower.
Otherwise, make honey (because there is a honeycomb).
'''

# When run

for i in range(4):
    bee.forward(3)
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()
    bee.right()


# Keep this
done()