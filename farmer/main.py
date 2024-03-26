from maze import *
from levels import LEVELS

maze = Maze(LEVELS["4-5 Bee Conditionals 3"])
bee = maze.player

def solution_1():
  bee.go_forward()
  bee.go_forward()
  bee.go_forward()
  if (bee.at_flower()):
    bee.get_nectar()

def solution_2():
  bee.go_forward()
  bee.go_forward()
  bee.right()
  for i in range(2):
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()

def solution_3():
  for i in range(2):
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()
    bee.left()


solution_3()

done()
