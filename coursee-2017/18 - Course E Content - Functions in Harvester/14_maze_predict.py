from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions11_predict")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/14

Figure out which function to use and which one to delete, then solve this puzzle!

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

while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this
while not farmer.has_pumpkin():
    # Do this
for i in range(5):
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

#
# Functions


```
'''

# When run

def wander_path():
    while farmer.path_ahead():
        farmer.forward()
    check_and_pick()

def find_pumpkin():
    while not farmer.at_pumpkin():
        farmer.forward()
    farmer.right()

def check_and_pick():
    if farmer.has_corn():
        farmer.pick_corn()
    else:
        if farmer.has_lettuce():
            farmer.pick_lettuce()
        else:
            if farmer.has_pumpkin():
                farmer.pick_pumpkin()

# Start
find_pumpkin()
wander_path()
find_pumpkin()
wander_path()
find_pumpkin()
wander_path()
check_and_pick()

# Keep this
Puzzle.done()