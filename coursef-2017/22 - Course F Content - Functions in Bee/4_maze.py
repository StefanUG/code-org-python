from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_conditionals3")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/4

You can only collect nectar from flowers, but you can check any space to see if there is a flower. If there is a flower under any of these clouds, the bee will need to collect nectar **once**.

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