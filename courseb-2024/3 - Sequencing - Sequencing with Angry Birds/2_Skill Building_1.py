from maze import Puzzle, Bird

maze = Puzzle.from_file("coursea_maze_ramp1_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/3/levels/2

To get the bird to the pig, snap the <xml><block type="maze_moveEast" block-text="move east"/></xml> block to the bottom of the <xml><block type="when_run" block-text="when run"/></xml> block, then press "▶ Run"!

---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

bird.east()
# Start

# Keep this
Puzzle.done()