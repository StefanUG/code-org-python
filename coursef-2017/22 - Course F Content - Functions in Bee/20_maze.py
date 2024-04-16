from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions7")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/20

Rebuild your function from the last puzzle to solve this maze.

Turn left at the honeycomb and right at the flowers.  
**Note:** Some corners are unmarked!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.make_honey()

#
# Loops

while bee.path_ahead():
    # Do this
for i in range(1):

while bee.nectar() > 0:
    # Do this
1

#
# Conditionals

if bee.path_right():
    # Do this
if bee.path_ahead():
    # Do this
else:
    # Otherwise this
if bee.at_flower():
    # Do this
if bee.at_flower():
    # Do this
else:
    # Otherwise this

#
# Functions

do_something()

#
# Math

1
1+1
```
'''

# When run

# Start

# Keep this
Puzzle.done()