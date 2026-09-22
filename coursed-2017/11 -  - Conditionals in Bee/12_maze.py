from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals9")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/11/levels/12

Collect all of the nectar or make all the honey. You can only collect nectar from flowers and make honey from honeycombs. Check any space to see if there is a flower or honeycomb. There will only ever be one flower or one honeycomb behind each cloud.

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