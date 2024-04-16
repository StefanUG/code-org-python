from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_for3_predict1")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/19/levels/4



---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar()

#
# Math

???
???*???

#
# Loops

for counter in range(1, 11, 1):

for i in range(): # limit: 1
    # Do this

#
# Variables

counter
```
'''

# When run

# Start
for counter in range(1, 5, 1):
    bee.forward()
    for i in range(counter):
        bee.get_nectar()

# Keep this
Puzzle.done()