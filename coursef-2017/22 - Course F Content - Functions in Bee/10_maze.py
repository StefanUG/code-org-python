from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_conditionals10")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/10

Conditionals can be helpful, even when you know exactly what is in each spot!

Collect all of the nectar and make all of the honey.

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

1

#
# Conditionals

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