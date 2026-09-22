from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging3")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/4

*"Be persistent and you will figure this out."*

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
collector.collect() # limit: 1
```
'''

# When run

# Start
for i in range(5):
    collector.forward()
    collector.collect()

# Keep this
Puzzle.done()