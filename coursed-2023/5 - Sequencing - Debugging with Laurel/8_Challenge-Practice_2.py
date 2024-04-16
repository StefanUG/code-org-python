from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging8a_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/5/levels/8

*"So much treasure!"*

Help Laurel fix the code to get all the treasure.

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
# 
```
'''

# When run

# Start
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.left()
collector.collect()
collector.collect()
collector.forward()
collector.collect()
collector.collect()
collector.collect()

# Keep this
Puzzle.done()