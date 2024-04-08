from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions1a_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/14/levels/3

*"Oooh, veggies are cropping up everywhere!"*

Now help the harvester pick all of the corn on the way to the pumpkin at the end.
___
##### Note: Every square on the way to the pumpkin either has **1** corn or nothing at all.  Use the provided `check for corn` function to make sure you get everything. 

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

player.forward()
player.right()
player.left()
player.pick_pumpkin()
player.pick_corn()

#
# Loops

while not player.at_pumpkin():
    # Do this
while player.has_corn():
    # Do this
while player.path_ahead():
    # Do this

#
# Conditionals

if player.path_ahead():
    # Do this
if player.path_ahead():
    # Do this
else:
    # Otherwise this
if player.has_corn():
    # Do this
else:
    # Otherwise this
if player.has_corn():
    # Do this
while not player.at_pumpkin():
    # Do this
while player.has_corn():
    # Do this
while player.path_ahead():
    # Do this

#
# Functions



#
# Comments

# 
```
'''

# When run

def check_square_for_corn():
    if farmer.has_corn():
        farmer.pick_corn()

# Start

# Keep this
Puzzle.done()