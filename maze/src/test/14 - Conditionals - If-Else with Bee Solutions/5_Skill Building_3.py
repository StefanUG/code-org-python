from maze import *

maze = Maze.from_file("courseD_bee_conditionals4_2023")
bee = maze.player

'''
In this puzzle, we know that every flower has exactly one nectar, but the flowers aren't spaced evenly.

Get all of the nectar using as few blocks as possible.


Get all of the nectar using as few blocks as possible.
'''

# When run

for i in range(7):
    bee.go_forward()
    if bee.at_flower():
        bee.get_nectar()


# Keep this
done()