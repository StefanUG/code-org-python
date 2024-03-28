from maze import *

maze = Maze.from_file("courseD_bee_conditionals_challenge2_2023")
bee = maze.player

'''
Collect all of the nectar and make all the honey. You can collect all of the nectar in one flower by using the `while nectar > 0` loop.


Collect all of the nectar and make all the honey.
'''

# When run

while bee.path_ahead():
    bee.go_forward()
    while bee.nectar() > 0:
        bee.get_nectar()
bee.right()
while bee.path_ahead():
    bee.go_forward()
    while bee.honey() > 0:
        bee.make_honey()
    


# Keep this
done()