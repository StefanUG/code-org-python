from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging9")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/9

*"It's treasure island!"*

Help Laurel fix the code to get all the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 2
collector.left() # limit: 2
collector.right()
collector.collect() # limit: 1
for i in range(???):
    # Do this
```
'''

# When run

# Start
for i in range(2):
    for i in range(3):
        collector.forward()
    collector.forward()
    for i in range(20):
        collector.collect()

# Keep this
Puzzle.done()