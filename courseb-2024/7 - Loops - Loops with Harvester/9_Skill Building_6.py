from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseA_harvester_loops6_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/7/levels/9

You will need **one** <xml><block type="maze_moveWest" block-text="move west"></block></xml> block and **one** <xml><block type="maze_moveNorth" block-text="move north"></block></xml> block to finish this puzzle!

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.pick_corn()
farmer.north() # limit: 1
farmer.west() # limit: 1
for i in range(5):
    # Do this
```
'''

# When run

# Start

# Keep this
Puzzle.done()