from maze import Puzzle, Farmer

maze = Puzzle.from_file("CourseD_2022_LessonExtra15b_2023")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2023/lessons/15/levels/16

*"I need some help on the farm! Help me harvest this corn using only the blocks in your toolbox."*

---
"I need some help on the farm! Help me harvest this corn using only the blocks in your toolbox."
'''

# When run

for i in range(3):
    for i in range(2):
        farmer.forward()
        farmer.left()
        farmer.forward()
        farmer.right()
    for i in range(5):
        farmer.pick_corn()


# Keep this
Puzzle.done()
