from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_debugging_challenge1a")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/11

*"Buzz buzz! I know how to get nectar, now help me make honey!"*

Watch how the bee gets the nectar. Can you use the same kind of pattern to help the bee make all of the honey?

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.backward()
bee.left()
bee.right()
bee.get_nectar() # limit: 1
bee.make_honey() # limit: 1
for i in range(3):
    # Do this
```
'''

# When run

# Start
for i in range(5):
    for i in range(2):
        bee.forward()
        bee.get_nectar()
    bee.backward()
for i in range(2):
    bee.forward()
    bee.right()

# Keep this
Puzzle.done()