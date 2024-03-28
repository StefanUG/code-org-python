from maze import *

maze = Maze.from_file("courseD_bee_conditionals2_2023")
bee = maze.player

'''
More clouds! 

Check underneath every cloud to see if it is hiding a flower before you get nectar. If there is a flower underneath the cloud, the bee will need to get nectar *once*.  

Remember: Not all clouds hide the same thing!


Check underneath every cloud to see if it is hiding a flower before you get nectar.  
'''

# When run

for i in range(2):
    bee.move_forward()

bee.right()

for i in range(2):
    bee.move_forward()
    if (bee.at_flower()):
        bee.get_nectar()



# Keep this
done()