from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions7a1_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/14/levels/8

*"Functions __lettuce__ do more with less work!"*

Create a function that sends the harvester down a square path to pick a single head of lettuce from the middle of each row.

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

for i in range(5):
    # Do this
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



# Keep this
Puzzle.done()