from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_conditionals_challenge1_2023")
bee = maze.player


'''
Collect all of the nectar and make all of the honey. You can only collect nectar from flowers and make honey from honeycombs. Check every space to see if there is a flower or honeycomb.


Collect all the nectar and make all the honey.
'''

# When run

while bee.path_ahead():
    if bee.at_flower():
        bee.get_nectar()
    elif bee.at_honeycomb():
        bee.make_honey()
    bee.go_forward()

    if not bee.path_ahead():
        bee.right()

# Keep this
maze.done()