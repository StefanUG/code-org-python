from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions3c_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/14/levels/6

Great!  Try your functions out on a longer path.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

player.forward()
player.right()
player.left()
player.pick_corn()
player.pick_pumpkin()
player.pick_lettuce()

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

def get_all_pumpkins():
    while farmer.has_pumpkin():
        farmer.pick_pumpkin()

def check_square_for_corn():
    if farmer.has_corn():
        farmer.pick_corn()

# Start

# Keep this
Puzzle.done()