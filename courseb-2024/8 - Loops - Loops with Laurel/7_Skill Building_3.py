from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops5_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/7

Add to the code from the last puzzle to get all of the treasure. 

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east() # limit: 2
collector.west()
collector.north()
collector.south() # limit: 1
for i in range(3):
    # Do this
collector.collect()
```
'''

# When run

# Start
for i in range(4):
    collector.east()
    collector.collect()
collector.south()
collector.collect()
collector.east()
collector.collect()

# Keep this
Puzzle.done()