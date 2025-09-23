from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming2_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2024/lessons/3/levels/3

Drag an extra <xml><block type="maze_moveForward" block-text="move forward"/></xml> block out of the toolbox to finish your code.

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