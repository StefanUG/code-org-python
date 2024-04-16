from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging6a_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/5/levels/7

Challenge: Use the code in the work area to get at least **6** pieces of treasure!

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.right()
collector.left()
collector.collect()
for i in range(5):
    # Do this
# 
```
'''

# When run

# Start
collector.forward()
collector.forward()
collector.collect()
collector.collect()

# Keep this
Puzzle.done()