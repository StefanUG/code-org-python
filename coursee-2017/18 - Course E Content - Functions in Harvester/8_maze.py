from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions6c")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/8

*"Lettuce pick all of the produce!"*

Now the sprouts can be either corn **or** lettuce.  What do you need to add to this program to check each sprout before you pick?
___
##### Note: Each sprout will turn into either **one** corn or **one** lettuce.

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

def corn_and_pumpkin():
    while not farmer.at_pumpkin():
        harvester_ifHasCorn
        farmer.forward()
    farmer.pick_pumpkin()

# Start
while farmer.path_ahead():
    corn_and_pumpkin()
    farmer.left()
    corn_and_pumpkin()
    farmer.right()

# Keep this
Puzzle.done()