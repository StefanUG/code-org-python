from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions6")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/18

*"This field is a-MAZE-ing!"*

Build your own function to help the bee through the maze by turning left at flowers and right at honeycomb.  Don't forget to collect nectar and make honey along the way!

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
while bee.nectar() > 0:
    # Do this

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