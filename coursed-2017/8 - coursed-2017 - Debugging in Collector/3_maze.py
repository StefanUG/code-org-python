from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging2")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/3

*"You can do this!"*

Fix the error(s) to collect all of the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 1
collector.right() # limit: 1
collector.left()
for i in range(???):
    # Do this
collector.collect() # limit: 1
```
'''

# When run

# Start
for i in range(3):
    collector.forward()
    collector.collect()

# Keep this
Puzzle.done()