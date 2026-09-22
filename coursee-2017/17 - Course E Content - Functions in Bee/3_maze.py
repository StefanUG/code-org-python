from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/3

Functions are blocks of code that perform a task.  

Use the `get 2 nectar` function to collect the nectar from each flower.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
for i in range(???):
    # Do this
get_2_nectar()
```
'''

# When run

def get_2_nectar():
    bee.get_nectar()
    bee.get_nectar()

# Start

# Keep this
Puzzle.done()