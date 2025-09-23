from maze import Puzzle, Bird

maze = Puzzle.from_file("courseD_maze_ramp2")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/2/levels/3

Drag an extra `move forward` block out of the toolbox, then attach all blocks to `when run` to finish your code.

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward() # limit: 3
```
'''

# When run

bird.forward()
bird.forward()
# Start

# Keep this
Puzzle.done()