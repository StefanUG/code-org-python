from maze import *

maze = Maze.from_file("courseD_bee_conditionals7_2023")
bee = maze.player

'''
Sometimes a cloud covers a flower, sometimes it covers a honeycomb! 

Use the `if/else` block to collect nectar at flowers and make honey at honeycomb. Remember: if there is a flower, the bee only needs to get nectar *once*. If there is a honeycomb, the bee only needs to make honey *once*.


Use the `if/else` block to collect nectar at flowers and make honey at honeycomb.
'''

# When run

bee.forward(2)
if bee.at_flower():
    bee.get_nectar()
else:
    bee.make_honey()

# Keep this
done()