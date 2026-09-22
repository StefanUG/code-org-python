from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions3c")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/5

Now, fill-in the function yourself by pulling the blocks from the code and dropping them into the **function definition**.  

Don't forget to add the little **function call** blocks to use the function in your program when you're done.

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


# Start
while not farmer.at_pumpkin():
    harvester_ifHasCorn
    farmer.forward()
farmer.pick_pumpkin()
farmer.left()
farmer.forward()
farmer.forward()
farmer.left()
while not farmer.at_pumpkin():
    harvester_ifHasCorn
    farmer.forward()
farmer.pick_pumpkin()
farmer.right()
while not farmer.at_pumpkin():
    harvester_ifHasCorn
    farmer.forward()
farmer.pick_pumpkin()
farmer.right()
while not farmer.at_pumpkin():
    harvester_ifHasCorn
    farmer.forward()
farmer.pick_pumpkin()

# Keep this
Puzzle.done()