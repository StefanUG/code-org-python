from maze import *

maze = Maze.from_file("courseD_bee_conditionals9_2023")
bee = maze.player

'''
Collect all of the nectar or make all the honey. You can only collect nectar from flowers and make honey from honeycombs. Check any space to see if there is a flower or honeycomb. There will only ever be one flower or one honeycomb behind each cloud.


Collect all of the nectar or make all the honey.
'''

# When run

for i in range(7):
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()


# Keep this
done()