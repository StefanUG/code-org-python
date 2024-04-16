from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp6")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/6

You can make code shorter and more efficient when you combine functions with other programming elements.  
___
What blocks can you use with your function to build a short and sweet solution to this puzzle?

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
for counter in range(1, 11, 1):

counter

#
# Conditionals

if bee.at_flower():
    # Do this

#
# Functions

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
rowOfNectar(length=?)

# Keep this
Puzzle.done()