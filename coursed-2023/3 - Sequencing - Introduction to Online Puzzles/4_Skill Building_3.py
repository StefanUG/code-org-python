from maze import Puzzle, Bird

maze = Puzzle.from_file("courseD_maze_ramp3_2023")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/3/levels/4

Help the bird get to the pig. There is one extra blue `move forward` block.

Throw away the extra block by removing it from the other blocks and dragging it back to the toolbox.

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