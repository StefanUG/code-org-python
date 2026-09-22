from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions4b")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/6

Use your new function to solve this puzzle.

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
for i in range():
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

def corn_and_pumpkin():
    while not farmer.at_pumpkin():
        harvester_ifHasCorn
        farmer.forward()
    farmer.pick_pumpkin()


# Keep this
Puzzle.done()