from maze import Puzzle, Collector

maze = Puzzle.from_file("courseC_collector_prog4_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2024/lessons/5/levels/5

*"Sequence matters!"*

The blocks you need are already in the workspace, but not connected.  

Put these blocks in order to collect all of the treasure and solve the puzzle.

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

collector.collect()
collector.forward()
collector.forward()
collector.left()
collector.collect()
collector.forward()
collector.forward()
collector.right()
collector.forward()
# Start

# Keep this
Puzzle.done()