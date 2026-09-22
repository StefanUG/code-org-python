from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging10_predict1")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/10

*"It's treasure island!"*

Help Laurel fix the code to get all the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
```
'''

# When run

# Start
for i in range(2):
    for i in range(3):
        collector.forward()
    for i in range(15):
        collector.collect()
    collector.left()

# Keep this
Puzzle.done()