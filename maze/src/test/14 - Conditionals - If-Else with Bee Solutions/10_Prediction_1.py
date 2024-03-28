from maze import *

maze = Maze.from_file("courseD_bee_conditionals7_predict2_2023")
bee = maze.player

'''
Sometimes a cloud covers a flower, sometimes it covers a honeycomb! 

Use the `if/else` block to collect nectar at flowers and make honey at honeycomb. Remember: there will only ever be *one* honeycomb or *one* flower behind each cloud.


Use the `if/else` block to collect nectar at flowers and make honey at honeycomb.
'''

# When run

for i in range(3):
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()


# Keep this
done()