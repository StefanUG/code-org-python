from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals1_predict1_2023")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/14/levels/2

*"This cloud is blocking my view!"*

Check to see if there's a flower under the cloud. If there's a flower, get nectar.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.make_honey()
for i in range(???):
    # Do this
if bee.at_flower():
    # Do this
```
'''

# When run

# Start
for i in range(3):
    bee.forward()
if bee.at_flower():
    bee.get_nectar()

# Keep this
Puzzle.done()