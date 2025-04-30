#from code_blocks import generate_python_from_blocks, generate_toolbox_python
import xml.etree.ElementTree as ET
import os
#
#
# # root = ET.parse("/Users/sgrinsted/ws/codingpirates/code-dot-org/dashboard/config/levels/custom/maze/courseD_farmer_while_challenge1_2023.level")
# root = ET.parse("/Users/sgrinsted/ws/codingpirates/code-dot-org/dashboard/config/levels/custom/maze/courseD_maze_until10_2023.level")
#
# solution = root.find("./blocks/solution_blocks/xml")
#
# code = generate_python_from_blocks(solution, player="zombie")
#
# print(code)


def chorus():
    print("doo doo, doo doo doo doo")


for person in ("Baby", "Mommy"):
    for i in range(4):
        print(person + " Shark")
        chorus()

