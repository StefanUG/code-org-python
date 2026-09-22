from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseD_farmer_condLoops4")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/13/levels/4

*"Gosh! Now the lettuce is growing in clusters!"*  

The harvester wants to pick everything from her lettuce garden. Each plant will now have more than one head of lettuce on it, so the farmer will need to keep picking while there is still lettuce growing.  

##### (Remember: This garden only has lettuce!)

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
if farmer.has_lettuce():
    # Do this
else:
    # Otherwise this
if farmer.has_lettuce():
    # Do this
farmer.pick_lettuce()
while farmer.path_ahead():
    # Do this
harvester_whileHasLettuce
for i in range(5):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()