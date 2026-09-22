from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_ramp14")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/12/levels/8

The same technique works with nectar and honey!  

Look at all of these clouds. Some of them will turn into honey, and others into nectar.   
Help the bee follow the path and solve this puzzle.





---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.right()
bee.left()
for i in range(5):
    # Do this
if bee.path_ahead():
    # Do this
else:
    # Otherwise this
while bee.nectar() > 0:
    # Do this
while bee.honey() > 0:
    # Do this
bee.get_nectar()
bee.make_honey()
```
'''

# When run

# Start

# Keep this
Puzzle.done()