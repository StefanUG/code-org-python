from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp3")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/3

Time to put the function to the test! 

Let's see if it makes collecting these three rows of nectar any easier.

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

rowOfNectar()
def rowOfNectar():



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

# Keep this
Puzzle.done()