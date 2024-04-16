from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/2

Here's some code that solves the last puzzle.  
Let's pull it into a function, then call the function to check this row for nectar.  
___
This may seem like a strange step now, but it will be really helpful soon!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward() # limit: 1
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


# Start
for i in range(7):
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()

# Keep this
Puzzle.done()