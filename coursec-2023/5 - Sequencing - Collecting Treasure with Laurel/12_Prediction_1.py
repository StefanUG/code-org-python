from maze import Puzzle, Collector

maze = Puzzle.from_file("grade2_collector_A_predict1_2023")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2023/lessons/5/levels/12



---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.right()
collector.left()
for i in range(???):
    # Do this
collector.collect()
```
'''

# When run

# Start
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()