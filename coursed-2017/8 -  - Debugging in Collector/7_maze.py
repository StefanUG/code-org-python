from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging6")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/7

**Challenge:**  All of the blocks that you need are already here...Now use your debugging skills to fix the errors and collect all of the treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 2
collector.left() # limit: 2
collector.right() # limit: 2
collector.collect() # limit: 1
for i in range(???): # limit: 2
    # Do this
```
'''

# When run

# Start
for i in range(5):
    collector.left()
    for i in range(5):
        collector.forward()
        collector.right()
    collector.forward()
    collector.collect()

# Keep this
Puzzle.done()