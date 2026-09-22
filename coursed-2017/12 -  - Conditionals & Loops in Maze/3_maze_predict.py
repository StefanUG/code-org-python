from maze import Puzzle, Bird

maze = Puzzle.from_file("courseD_maze_until2_predict1")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/12/levels/3



---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward() # limit: 1
bird.right()
bird.left()
while bird.path_ahead():
    # Do this
while not bird.at_finish():
    # Do this
```
'''

# When run

# Start
while not bird.at_finish():
    while bird.path_ahead():
        bird.forward()
    bird.left()

# Keep this
Puzzle.done()