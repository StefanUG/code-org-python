from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_functions4")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/15

Did you know that you can call a function from *inside* another function?  

Use your `check nectar or honey` function inside the new `move and check` function to help the bee turn, go get what's under the cloud, then back-up and turn back around!

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
bee.make_honey() # limit: 1

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