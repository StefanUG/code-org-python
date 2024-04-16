from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_conditionals2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/3

*"It's too cloudy to see any flowers!"*

Check underneath every cloud to see if it is hiding a flower before you get nectar. If there is a flower underneath the cloud, the bee will need to get nectar **once**.  

Remember: Not all clouds hide the same thing!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar() # limit: 1
bee.make_honey() # limit: 0

#
# Loops

for i in range(1): # limit: 1

1
while bee.path_ahead():
    # Do this

#
# Conditionals

if bee.at_flower():
    # Do this
if bee.at_flower():
    # Do this
else:
    # Otherwise this
while bee.path_ahead():
    # Do this

#
# Functions

do_something()
move_and_check()
get_only_nectar()
def move_and_check():
    bee.right()
    bee.forward()
    check_nectar_or_honey()
    bee.backward()
    bee.left()

def check_nectar_or_honey():
    if bee.at_flower():
        bee.get_nectar() # limit: 1
    else:
        bee.make_honey() # limit: 1


#
# Math

1
1+1
```
'''

# When run

bee.forward()
bee.forward()
bee.left()
bee.forward()
if bee.at_flower():
    # Do this
bee.get_nectar()
for i in range():
    # Do this
2
# Start

# Keep this
Puzzle.done()