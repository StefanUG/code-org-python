from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions5a")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/16

Now, build `move and check` so that it takes the bee to the cloud whenever there is a path to the right, then use it to solve this puzzle!

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
if bee.path_right():
    # Do this

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

def check_nectar_or_honey():
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()

def move_and_check():


move_and_check()
# Start

# Keep this
Puzzle.done()