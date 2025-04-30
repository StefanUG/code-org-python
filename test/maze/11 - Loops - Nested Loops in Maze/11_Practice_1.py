from maze import Puzzle

maze = Puzzle.from_file("courseD_bee_nestedLoops8_2023")
bee = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/11/levels/11

Collect all of the nectar from each flower and make honey at the honeycomb. 

---
Collect all of the nectar from each flower and make honey at the honeycomb. 
'''

# When run


for j in range(5):
    bee.forward()
    for i in range(4):
        bee.get_nectar()

bee.forward()

for n in range(4):
    bee.make_honey()


# Keep this
maze.done()