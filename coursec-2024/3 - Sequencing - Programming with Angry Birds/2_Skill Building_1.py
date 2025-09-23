from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming1_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2024/lessons/3/levels/2

For this puzzle, drag all of the blocks together and click "Run" to watch it go!

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward() # limit: 4
```
'''

# When run

bird.forward()
bird.forward()
# Start

# Keep this
Puzzle.done()