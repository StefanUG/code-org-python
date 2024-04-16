from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseF_bee_fwp_challenge2")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/11

*"**Lettuce** see if you can handle this one final test! Give it everything you've got!"*

Use one `for loop` in a function to collect all of the vegetables in the row. Make the `for loop` count to different maximum values by using the `length` parameter. Make your program as short as possible by using a second `for loop` outside the function.

Good luck!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

farmer.forward() # limit: 7
farmer.right()
farmer.left()
farmer.pick_pumpkin() # limit: 1
farmer.pick_corn() # limit: 1
farmer.pick_lettuce() # limit: 1

#
# Loops

for i in range():
    # Do this
for counter2 in range(1, 7, 1):

counter2

#
# Conditionals

if farmer.has_lettuce():
    # Do this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this

#
# Functions



#
# Math

1
```
'''

# When run

def pick_row(length):
    farmer.left()
    for counter in range(1, length+1, 1):
        farmer.forward()
        for i in range(counter):
            farmer.pick_corn()
    for i in range(length):
        farmer.backward()
    farmer.right()

# Start
farmer.forward()
pick_row(length=1)

# Keep this
Puzzle.done()