from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging4a_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/5/levels/5

*"Don't get frustrated. You can do it!"*

Fix the error(s) to collect all of the treasure.

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
collector.collect()
collector.left()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()