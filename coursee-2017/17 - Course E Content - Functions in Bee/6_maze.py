from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions5")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/6



---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left() # limit: 2
bee.right() # limit: 2
bee.get_nectar() # limit: 1
bee.make_honey()
for i in range(???):
    # Do this
move_and_get_4()
```
'''

# When run

def move_and_get_4():


# Start
bee.forward()
move_and_get_4()
bee.forward()
for i in range(2): # limit: 2
    bee.forward()
    move_and_get_4()

# Keep this
Puzzle.done()