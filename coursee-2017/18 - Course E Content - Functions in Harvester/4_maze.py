from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions2ba")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/4

*"I feel so functional!"*

Did you notice that there was repeated code in the last puzzle?  It doesn't work to put it all inside of a loop, but we **can** use functions.  

For this puzzle, we have moved the repeated code into a function called `corn and pumpkin`. Now, all you need to do is put the small `corn and pumpkin` **function call block** into the code where you need it.

___
##### Each sprout will either grow *one* corn or nothing.

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

corn_and_pumpkin()
farmer.left()
farmer.forward()
farmer.forward()
farmer.left()
corn_and_pumpkin()
# Start

# Keep this
Puzzle.done()