from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging5")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/6

*"This puzzle is making me loopy!"*

All of the commands that you need are already here...now use your debugging skills to figure out how to solve this puzzle.

---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

# Start
for i in range(2):
    collector.forward()
    collector.collect()
    collector.forward()
for i in range(3):
    collector.right()

# Keep this
Puzzle.done()