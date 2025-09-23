from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops2_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/3

Move Laurel to the treasure, then use the <xml><block type="collector_collect" block-text="get treasure"/></xml> block to pick it up.


Get all four piles to pass this level.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east()
collector.west()
collector.north()
collector.south()
collector.collect()
for i in range(5):
    # Do this
```
'''

# When run



# Keep this
Puzzle.done()