from maze import Puzzle, Bird

maze = Puzzle.from_file("courseD_maze_ramp3")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/2/levels/4

*"This pig is ruffling my feathers."*

There is one extra block that is going to cause the bird to crash.  
Throw it away by removing it from the other blocks and dragging it back to the toolbox.

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