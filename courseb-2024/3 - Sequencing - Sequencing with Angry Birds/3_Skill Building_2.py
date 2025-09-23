from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_ramp2_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/3/levels/3

Attach both <xml><block type="maze_moveEast" block-text="move east"/></xml> blocks to the <xml><block type="when_run" block-text="when run"/></xml> block to finish your code, then click "▶ Run".

---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

bird.east()
bird.east()
# Start

# Keep this
Puzzle.done()