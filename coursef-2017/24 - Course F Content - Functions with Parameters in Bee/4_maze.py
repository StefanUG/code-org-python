from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp4")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/4

*"How is your function holding up?"*   

We need to make some adjustments here. Click "edit" to add a `length` parameter to the function so that it will still work when the row is a different length.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar() # limit: 1

#
# Loops

for i in range(1):

1

#
# Conditionals

if bee.at_flower():
    # Do this
if bee.path_ahead():
    # Do this
if bee.path_ahead():
    # Do this
else:
    # Otherwise this

#
# Functions

1
def rowOfNectar():


rowOfNectar()

#
# Math

1
1+1
```
'''

# When run

def rowOfNectar():
    for i in range(7):
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()

# Start
rowOfNectar()
bee.right()
bee.forward()
bee.forward()
bee.right()
rowOfNectar()
bee.left()
bee.forward()
bee.forward()
bee.left()
rowOfNectar()

# Keep this
Puzzle.done()