from maze import Puzzle, Collector

maze = Puzzle.from_file("courseC_collector_prog7_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/5/levels/8

**Challenge:** *"What is going on here?"*

Even if we put these in the right order, there will still be some missing.  
Use blocks from the toolbox to collect all of the treasure.

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
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.forward()
collector.right()

# Keep this
Puzzle.done()