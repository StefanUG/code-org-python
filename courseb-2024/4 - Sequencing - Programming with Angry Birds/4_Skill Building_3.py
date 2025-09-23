from maze import Puzzle, Bird

maze = Puzzle.from_file("courseA_maze_seq5a_2024")
bird: Bird = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/4/levels/4

*"Here piggy, piggy!"*

What can you add to the end of this code to get the bird to the pig?

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.north()
bird.south()
bird.east()
bird.west()
for i in range(3):
    # Do this
```
'''

# When run

# Start
bird.south()
bird.south()
bird.south()

# Keep this
Puzzle.done()