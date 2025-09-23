from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_nestedLoops9_predict2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/8/levels/13

Make all of the honey.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
bee.get_nectar()
bee.make_honey() # limit: 1
for i in range(???):
    # Do this
```
'''

# When run

# Start
for i in range(2):
    for i in range(2):
        bee.forward()
        bee.make_honey()
    bee.left()
    for i in range(2):
        bee.forward()
        bee.make_honey()
    bee.right()

# Keep this
Puzzle.done()