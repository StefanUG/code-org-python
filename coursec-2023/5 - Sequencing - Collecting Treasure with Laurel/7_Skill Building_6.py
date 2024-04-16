from maze import Puzzle, Collector

maze = Puzzle.from_file("courseC_collector_prog6_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/5/levels/7

*"Help me collect all of the treasure!"*

These blocks are in the wrong order. Reorder them to collect all of the treasure.

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
collector.forward()
collector.right()
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.forward()

# Keep this
Puzzle.done()