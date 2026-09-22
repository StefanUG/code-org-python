from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions1a")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/2

*"Oooh, veggies are cropping up everywhere!"*

Now help the harvester pick all of the corn on the way to the pumpkin at the end.
___
##### Note: Every square on the path that leads to the pumpkin will either have *one* corn or nothing.  You will need to use an `if` statement to check whether there is corn before you try to pick it!

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



# Keep this
Puzzle.done()