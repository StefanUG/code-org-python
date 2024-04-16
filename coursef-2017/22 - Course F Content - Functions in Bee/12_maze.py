from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/12

To make things easier, it's time to learn about functions!

From here on out, you will be using a new *function editor*.  This editor is a separate window that will appear when you go to edit a function.  You won't see all of the code from your function while you're coding in the workspace, but don't worry...it's still there!  
___

Let's practice with this function that gets nectar only if the bee is at a flower.  To see the code inside, click the blue "edit" button!

Use the `get only nectar` function to collect the nectar from each flower.

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

def get_only_nectar():
    if bee.at_flower():
        bee.get_nectar()

get_only_nectar()
# Start

# Keep this
Puzzle.done()