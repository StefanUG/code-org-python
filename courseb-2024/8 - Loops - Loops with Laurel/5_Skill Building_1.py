from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops3_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/5

How can Laurel get all five piles of treasure using only one <xml><block type="maze_moveEast" block-text="move east"/></xml> block?

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east() # limit: 1
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