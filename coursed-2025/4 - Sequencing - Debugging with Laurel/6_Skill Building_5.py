from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging5a_2025")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/4/levels/6

*"This puzzle is making me loopy!"*

All of the commands that you need are already here...now use your debugging skills to figure out how to solve this puzzle.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.right()
collector.left()
collector.collect()
for i in range(???):
    # Do this
```
'''

# When run

# Start
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.right()
collector.right()
collector.collect()
collector.collect()
collector.collect()
collector.collect()
collector.collect()
collector.collect()

# Keep this
Puzzle.done()