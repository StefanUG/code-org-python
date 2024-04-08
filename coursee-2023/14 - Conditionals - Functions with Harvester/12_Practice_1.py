from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions13_2023")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2023/lessons/14/levels/12

Solve this puzzle in 23 blocks or less.
___  

##### Each sprout will either grow *one* corn or nothing. To find the best solution, you will need to edit the functions directly.

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
player.pick_lettuce()

#
# Loops

for i in range(???):
    # Do this
while not player.at_pumpkin():
    # Do this
while player.has_corn():
    # Do this
while player.has_lettuce():
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
if player.has_lettuce():
    # Do this
if player.has_corn():
    # Do this
while not player.has_lettuce():
    # Do this
while player.has_corn():
    # Do this
while player.has_lettuce():
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

def check_for_corn():
    if farmer.has_corn():
        farmer.pick_corn()

def pick_along_path():
    while not farmer.has_pumpkin():
        check_for_corn()
        farmer.forward()

# Start

# Keep this
Puzzle.done()