from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_ramp3a_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/3/levels/4

Grab a <xml><block type="maze_moveNorth" block-text="move north"/></xml> block from the toolbox and add it to the bottom of the other blocks to finish this code, then click "▶ Run".

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.north()
```
'''

# When run

# Start
bird.east()
bird.east()

# Keep this
Puzzle.done()