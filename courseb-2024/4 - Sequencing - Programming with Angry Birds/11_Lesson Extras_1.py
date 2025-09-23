from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_seq_challenge1_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/4/levels/11

Debug this level. Remove the extra blocks, and add the missing blocks. Get the bird to the pig!

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
bird.south()
bird.south()
bird.east()
bird.east()
bird.north()
bird.north()

# Keep this
Puzzle.done()