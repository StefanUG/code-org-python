from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions8b")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/11

**Challenge:** Not all corners are marked in this maze, that means that you will need to use your navigation code more than once to get where you need to go.  

Can you figure out what you need to do?

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

farmer.forward()
farmer.right()
farmer.left()
farmer.pick_corn()
farmer.pick_pumpkin()
farmer.pick_lettuce()

#
# Loops

while not farmer.at_pumpkin():
    # Do this
while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this

#
# Conditionals

if farmer.path_ahead():
    # Do this
if farmer.path_ahead():
    # Do this
else:
    # Otherwise this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
if farmer.has_corn():
    # Do this
while not farmer.at_pumpkin():
    # Do this
while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this

#
# Functions


```
'''

# When run

# Start
while not farmer.at_pumpkin():
    farmer.forward()
    if farmer.has_corn():
        farmer.pick_corn()
        farmer.left()
    else:
        if farmer.has_lettuce():
            farmer.pick_lettuce()
            farmer.right()
farmer.pick_pumpkin()

# Keep this
Puzzle.done()