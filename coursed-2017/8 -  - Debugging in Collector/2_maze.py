from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging1")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/2

*"Oh no! I see a problem."*

Fix the error(s) to collect all of the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 2
collector.right()
collector.left()
for i in range(???):
    # Do this
collector.collect() # limit: 2
```
'''

# When run

# Start
collector.forward()
collector.collect()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()