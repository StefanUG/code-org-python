from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp5")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/5

*"You're doing great so far!"*

Let's use this function to collect the nectar.

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
if bee.path_left():
    # Do this
if bee.path_left():
    # Do this
else:
    # Otherwise this

#
# Functions

def rowOfNectar():


1
rowOfNectar()

#
# Math

1
1+1
```
'''

# When run

def rowOfNectar(length):
    for i in range(length):
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()

# Start
rowOfNectar(length=2)

# Keep this
Puzzle.done()