from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging3a_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/5/levels/4

*"Be persistent and you will figure this out."*

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
collector.forward()
collector.collect()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()