from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals7_2023")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/14/levels/9

Sometimes a cloud covers a flower, sometimes it covers a honeycomb! 

Use the `if/else` block to collect nectar at flowers and make honey at honeycomb. Remember: if there is a flower, the bee only needs to get nectar *once*. If there is a honeycomb, the bee only needs to make honey *once*.

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
for i in range(???):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()