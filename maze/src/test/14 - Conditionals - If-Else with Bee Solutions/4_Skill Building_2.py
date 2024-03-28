from maze import *

maze = Maze.from_file("courseD_bee_conditionals3_2023")
bee = maze.player

'''
You can only collect nectar from flowers, but you can check any space to see if there is a flower. If there is a flower under any of these clouds, the bee will need to collect nectar *once*.


Help the bee collect all of the nectar. 

You can only collect nectar from flowers, but you can check any space to see if there is a flower.
'''

# When run

for i in range(7):
    bee.go_forward()
    if bee.at_flower():
        bee.get_nectar()



# Keep this
done()