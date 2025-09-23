from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_ramp4a_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/3/levels/6

Can you figure out which block you need to add to the bottom of the other blocks to finish this code?

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.north()
bird.south()
bird.east()
bird.west()
```
'''

# When run

# Start
bird.east()
bird.east()

# Keep this
Puzzle.done()