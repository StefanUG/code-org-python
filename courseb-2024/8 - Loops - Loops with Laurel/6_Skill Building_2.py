from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops4_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/6

Fix Laurel's path to get all of this treasure!

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east() # limit: 2
collector.west()
collector.north()
collector.south()
collector.collect()
for i in range(5):
    # Do this
```
'''

# When run

# Start
for i in range(5):
    collector.east()
    collector.collect()
collector.south()
collector.collect()

# Keep this
Puzzle.done()