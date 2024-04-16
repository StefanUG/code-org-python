from maze import Puzzle, Collector

maze = Puzzle.from_file("courseC_collector_prog5_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/5/levels/6

*"Help me collect each bit of treasure!"*

These blocks are in the wrong order. Can you fix them?

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
collector.collect()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.forward()
collector.forward()

# Keep this
Puzzle.done()