from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_ramp3b_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/3/levels/5

There's an extra <xml><block type="maze_moveSouth" block-text="move south"/></xml> block at the end of this code!  

Drag it back to the toolbox to throw it away.

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.south()
bird.west()
```
'''

# When run

# Start
bird.south()
bird.west()
bird.west()
bird.south()

# Keep this
Puzzle.done()