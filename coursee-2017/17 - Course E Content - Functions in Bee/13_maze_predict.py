from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions11_predict1")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/13



---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
bee.get_nectar()
bee.make_honey()
for i in range(???):
    # Do this
while bee.honey() > 0:
    # Do this
move_and_make_honey()
def move_and_make_honey():


```
'''

# When run

def move_and_make_honey():
    bee.right()
    bee.forward()
    while bee.honey() > 0:
        bee.make_honey()
    bee.backward()
    bee.left()

# Start
move_and_make_honey()
for i in range(3):
    bee.forward()
move_and_make_honey()
bee.forward()
bee.forward()
move_and_make_honey()

# Keep this
Puzzle.done()