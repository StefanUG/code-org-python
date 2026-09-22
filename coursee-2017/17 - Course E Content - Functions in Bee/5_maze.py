from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions4")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/5

The `move and get nectar` function turns the bee, collects nectar, and then returns the bee to where it started.  

Use the `move and get nectar` function to collect all of the nectar.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
bee.make_honey()
for i in range(???): # limit: 1
    # Do this
move_and_get_nectar()
```
'''

# When run

def move_and_get_nectar():
    bee.right()
    bee.forward()
    bee.get_nectar()
    bee.backward()
    bee.left()

# Start

# Keep this
Puzzle.done()