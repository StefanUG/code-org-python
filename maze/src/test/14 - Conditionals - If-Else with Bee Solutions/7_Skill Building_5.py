from maze import *

maze = Maze.from_file("courseD_bee_conditionals6_2023")
bee = maze.player

'''
*"Now I just want to make honey."*

Some of these clouds might have honeycombs under them.  Be sure to check if a honeycomb is hiding behind each cloud! If there is a honeycomb, the bee will only need to make honey *once*.


Some of these clouds might have honeycombs under them.  Be sure to check if a honeycomb is hiding behind each cloud!
'''

# When run

for i in range(2):
    bee.forward()
    bee.forward()
    if bee.at_honeycomb():
        bee.make_honey()
    bee.left()

# Keep this
done()