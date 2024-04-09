from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming7_2023")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/3/levels/8

*"It's time to get angry!"*

**Challenge:** This code has a lot of bugs. You'll need to remove some blocks and add others.

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward()
bird.left()
bird.right()
for i in range(???):
    # Do this
```
'''

# When run

# Start
bird.forward()
bird.forward()
bird.right()
bird.forward()
bird.forward()
bird.left()
bird.forward()
bird.right()
bird.forward()
bird.forward()
bird.forward()
bird.forward()

# Keep this
Puzzle.done()