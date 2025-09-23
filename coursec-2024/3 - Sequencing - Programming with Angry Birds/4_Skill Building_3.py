from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming3_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2024/lessons/3/levels/4

*"This pig is ruffling my feathers."*

There is one extra block that is going to cause the bird to crash.  
Throw it away by unhooking it from the grey blocks and dragging it back to the toolbox.

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward() # limit: 4
bird.left() # limit: 1
bird.right() # limit: 1
```
'''

# When run

# Start
bird.forward()
bird.forward()
bird.left()
bird.forward()
bird.forward()

# Keep this
Puzzle.done()