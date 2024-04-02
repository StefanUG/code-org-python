from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_conditionals1_predict1_2023")
bee = maze.player

'''
*"This cloud is blocking my view!"*

Check to see if there's a flower under the cloud. If there's a flower, get nectar.


Check to see if there's a flower under the cloud. If there's a flower, get nectar.
'''

# When run

for i in range(3):
    bee.move_forward()
if bee.at_flower():
    bee.get_nectar()


# Keep this
maze.done()