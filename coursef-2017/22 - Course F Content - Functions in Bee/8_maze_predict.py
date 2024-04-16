from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_conditionals7_predict2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/22/levels/8

Sometimes a cloud covers a flower, sometimes it covers a honeycomb!

Use the `if/else` block to collect nectar at flowers and make honey at honeycomb.

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

# Start
while bee.path_ahead():
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()

# Keep this
Puzzle.done()