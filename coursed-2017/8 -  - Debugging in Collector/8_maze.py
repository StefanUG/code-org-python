from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging8")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/8

*"So much treasure!"*

Help Laurel fix the code to get all the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.left() # limit: 1
collector.right()
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
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.right()

# Keep this
Puzzle.done()