from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming3_2023")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/3/levels/4

*"This pig is ruffling my feathers."*

There is one extra block that is going to cause the bird to crash.  
Throw it away by unhooking it from the grey blocks and dragging it back to the toolbox.

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward()
bird.left()
bird.right()
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