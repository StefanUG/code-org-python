from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging1a_2025")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/4/levels/2

*"Oh no! I see a problem."*

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
collector.forward()
collector.forward()

# Keep this
Puzzle.done()