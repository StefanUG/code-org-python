from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_predict1")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/12/levels/4

Help the farmer walk the path to find all of the lettuce

In this puzzle, lettuce is growing at the end of every path.  If there is a path in front of her, the farmer can keep moving forward.  Otherwise, she needs to pick all of the lettuce, then turn to stay on the path. 





---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward() # limit: 1
farmer.right()
farmer.left()
if farmer.has_lettuce(): # limit: 1
    # Do this
else:
    # Otherwise this
while farmer.has_corn(): # limit: 2
    # Do this
while farmer.has_lettuce(): # limit: 2
    # Do this
farmer.pick_corn() # limit: 1
farmer.pick_lettuce() # limit: 1
```
'''

# When run

# Start
for i in range(15):
    if farmer.path_ahead():
        farmer.forward()
    else:
        while farmer.has_lettuce():
            farmer.pick_lettuce()
        farmer.left()

# Keep this
Puzzle.done()