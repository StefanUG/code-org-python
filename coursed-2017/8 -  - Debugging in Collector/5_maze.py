from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging4")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/5

*"Don't get frustrated. You can do it!"*

Fix the error(s) to collect all of the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.right()
collector.left()
for i in range(???):
    # Do this
collector.collect()
```
'''

# When run

# Start
for i in range(3):
    collector.forward()
    collector.collect()
    collector.right()
    collector.forward()
    collector.collect()

# Keep this
Puzzle.done()