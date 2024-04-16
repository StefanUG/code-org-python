from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions_challenge1")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/22

Create a new function to collect all the nectar and honey while there is a path ahead. Use it to complete the puzzle!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar() # limit: 2
bee.make_honey() # limit: 2

#
# Loops

for i in range(1):

1
while bee.path_ahead(): # limit: 1
    # Do this
while bee.honey() > 0: # limit: 2
    # Do this

#
# Conditionals

if bee.at_flower(): # limit: 2
    # Do this
if bee.at_flower(): # limit: 1
    # Do this
else:
    # Otherwise this

#
# Functions



#
# Math

1
def rowOfNectar():


```
'''

# When run

def row_of_nectar():


# Start
row_of_nectar()
bee.right()
bee.forward()
bee.forward()
bee.right()
row_of_nectar()
bee.left()
bee.forward()
bee.forward()
bee.left()
row_of_nectar()

# Keep this
Puzzle.done()