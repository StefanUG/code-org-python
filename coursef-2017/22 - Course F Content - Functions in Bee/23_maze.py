from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions_challenge2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/23

Use everything you have learned to complete this puzzle!

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
while bee.path_ahead(): # limit: 2
    # Do this
while bee.nectar() > 0: # limit: 2
    # Do this

#
# Conditionals

if bee.at_flower(): # limit: 2
    # Do this
if bee.path_right():
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

# Start

# Keep this
Puzzle.done()