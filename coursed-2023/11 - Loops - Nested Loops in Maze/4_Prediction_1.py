from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_nestedLoops2_predict1_2023")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/4

This time, help the bee collect all of the nectar using as few blocks as possible.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.right()
bee.left()
bee.get_nectar()
for i in range(5):
    # Do this
```
'''

# When run

# Start
for i in range(3):
    bee.forward()
    for i in range(2):
        bee.forward()
        bee.get_nectar()
    bee.right()

# Keep this
Puzzle.done()