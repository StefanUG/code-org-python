from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals7_predict2_2023")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/14/levels/10

Sometimes a cloud covers a flower, sometimes it covers a honeycomb! 

Use the `if/else` block to collect nectar at flowers and make honey at honeycomb. Remember: there will only ever be *one* honeycomb or *one* flower behind each cloud.

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
for i in range(3):
    bee.forward()
    if bee.at_flower():
        bee.get_nectar()
    else:
        bee.make_honey()

# Keep this
Puzzle.done()