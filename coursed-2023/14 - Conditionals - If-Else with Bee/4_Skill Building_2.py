from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals3_2023")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/14/levels/4

You can only collect nectar from flowers, but you can check any space to see if there is a flower. If there is a flower under any of these clouds, the bee will need to collect nectar *once*.

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
for i in range(???):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()