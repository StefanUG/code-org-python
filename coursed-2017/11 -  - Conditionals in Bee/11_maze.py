from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals8")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/11/levels/11

**Challenge:** There will be either a flower or a honeycomb under each of those clouds!

Collect nectar once if there is a flower.
Otherwise, make honey once (because there is a honeycomb).

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.make_honey()
if bee.at_flower():
    # Do this
else:
    # Otherwise this
while bee.path_ahead():
    # Do this
for i in range(???):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()