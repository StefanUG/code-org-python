from maze.maze import *
# from levels import LEVELS

# maze = Maze(LEVELS["4-5 Bee Conditionals 3"])

def solution_1():
  puzzle = Maze.from_file("courseD_bee_conditionals1_predict1_2023")
  bee = puzzle.player

  bee.go_forward()
  bee.go_forward()
  bee.go_forward()
  if (bee.at_flower()):
    bee.get_nectar()

def solution_2():
  maze = Maze.from_file("courseD_bee_conditionals2_2023")
  bee = maze.player

  bee.go_forward()
  bee.go_forward()
  bee.right()
  for i in range(2):
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()

def solution_3():
  maze = Maze.from_file("courseD_bee_conditionals3_2023")
  bee = maze.player

  for i in range(2):
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()
    bee.left()

def solution_4():
  maze = Maze.from_file("courseD_bee_conditionals4_2023")
  bee = maze.player

  for i in range(2):
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()
    bee.left()

def solution_5():
  maze = Maze.from_file("courseD_bee_conditionals5_2023")
  bee = maze.player

  for i in range(2):
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()
    bee.left()

def solution_6():
  maze = Maze.from_file("courseD_bee_conditionals6_2023")
  bee = maze.player

  for i in range(2):
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()
    bee.left()

def solution_7():
  maze = Maze.from_file("courseD_bee_conditionals7_2023")
  # maze = Maze.from_file("courseD_bee_conditionals7_predict2_2023")
  bee = maze.player

  for i in range(3):
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()

def solution_8():
  # https://studio.code.org/s/coursed-2023/lessons/14/levels/11
  maze = Maze.from_file("courseD_bee_conditionals8_2023")
  bee = maze.player

  for i in range(4):
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()

def solution_9():
  # https://studio.code.org/s/coursed-2023/lessons/14/levels/12
  maze = Maze.from_file("courseD_bee_conditionals9_2023")
  bee = maze.player

  for i in range(7):
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()


def xsolution_4():
    # https://studio.code.org/s/coursed-2023/lessons/14/levels/9
    bee.go_forward()
    bee.go_forward()
    if (bee.at_flower()):
      bee.get_nectar()
    if (bee.at_honeycomb()):
      bee.make_honey()

solution_9()

done()
