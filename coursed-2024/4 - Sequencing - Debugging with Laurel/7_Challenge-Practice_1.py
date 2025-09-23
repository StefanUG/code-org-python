from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging6a_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/4/levels/7

Challenge: Use the code in the work area to get at least **6** pieces of treasure!

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 10
collector.right() # limit: 6
collector.left() # limit: 6
collector.collect()
for i in range(5):
    # Do this
# 
```
'''

# When run

collector.left()
collector.left()
collector.left()
collector.left()
collector.left()
collector.right()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.forward()
collector.collect()
collector.collect()
collector.collect()
collector.collect()
collector.collect()
collector.collect()
# Start
collector.forward()
collector.forward()
collector.collect()
collector.collect()

# Keep this
Puzzle.done()