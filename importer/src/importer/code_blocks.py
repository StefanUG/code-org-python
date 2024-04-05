import xml.etree.ElementTree as ET
import jinja2
import textwrap
import sys


def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# Define the mapping from XML block types to Python constructs
BLOCK_MAPPING = {
    # Generally applicable blocks
    "when_run": "# Start",
    "controls_repeat": "for i in range({{field['TIMES']}}):\n{{statements['DO']}}",
    "comment": "# {{field['TEXT']}}",

    # Generic Maze blocks
    "maze_untilBlockedOrNotClear": "while {{field['DIR']}}:\n{{statements['DO']}}",
    "maze_moveForward":  "{{player}}.forward()",
    "maze_turn":         "{{player}}.{{field['DIR']}}",
    "maze_untilBlocked": "while {{player}}.path_ahead():\n{{statements['DO']}}",
    "maze_move":         "{{player}}.{{field['DIR']}}",
    "maze_ifElse":       "if {{player}}.{{field['DIR']}}:\n{{statements['DO']}}\nelse:{{statements['ELSE']}}",
    "maze_if":           "if {{player}}.{{field['DIR']}}:\n{{statements['DO']}}",
    "maze_forever":      "while not {{player}}.at_finish():\n{{statements['DO']}}",

    # Farmer related
    "maze_fill": "{{player}}.fill()",
    "maze_dig":  "{{player}}.remove()",

    # Harverster related
    "harvester_corn":    "{{player}}.pick_corn()",
    "harvester_lettuce": "{{player}}.pick_lettuce()",
    "harvester_pumpkin": "{{player}}.pick_pumpkin()",

    # Bee related
    "maze_honey":  "{{player}}.make_honey()",
    "maze_nectar": "{{player}}.get_nectar()",
    "bee_whileNectarAmount": "while {{field['ARG1']}} {{field['OP']}} {{field['ARG2']}}:",
    "bee_ifFlower":     "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}",
    "bee_ifElseFlower": "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}\nelse:\n{{statements['ELSE']}}",
}

FIELD_MAPPING = {
    # Generic Maze blocks
    "maze_turn/turnRight":    "right()",
    "maze_turn/turnLeft":     "left()",
    "maze_move/moveForward":  "forward()",
    "maze_move/moveBackward": "backward()",

    "maze_if/isPathForward":     "path_ahead()",
    "maze_if/isPathLeft":        "path_left()",
    "maze_if/isPathRight":       "path_right()",
    "maze_ifElse/isPathForward": "path_ahead()",

    "maze_untilBlockedOrNotClear/holePresent": "{{player}}.at_hole()",
    "maze_untilBlockedOrNotClear/pilePresent": "{{player}}.at_pile()",
    "maze_untilBlockedOrNotClear/isPathForward": "{{player}}.path_ahead()",

    "bee_whileNectarAmount/nectarRemaining": "{{player}}.nectar()",
    "bee_whileNectarAmount/honeyAvailable":  "{{player}}.honey()",
    "bee_whileNectarAmount/>": ">",
    "bee_whileNectarAmount/<": "<",
    "bee_whileNectarAmount/=": "==",

    "bee_ifFlower/atFlower": "at_flower()",
    "bee_ifFlower/atHoneycomb": "at_honeycomb()",
    "bee_ifElseFlower/atFlower": "at_flower()",
    "bee_ifElseFlower/atHoneycomb": "at_honeycomb()",
}

J2_ENVIRONMENT = jinja2.Environment()

def map_field(block_type, text, player):
    key = f"{block_type}/{text}"
    value = FIELD_MAPPING.get(key)
    if value:
        template = J2_ENVIRONMENT.from_string(value)
        value = template.render(player=player)
    else:
        if text == None:
            text = ""
        value = text
        print(f"     -- No FIELD_MAPPING found for key '{key}', using value from attribute '{value}'")

    return value


def map_block(block_type, field, player, statements=None) -> str:
    value = BLOCK_MAPPING.get(block_type)
    if not statements:
        statements = {"DO": "    # Do this", "ELSE": "    # Otherwise this"}
    if value:
        try:
            template = J2_ENVIRONMENT.from_string(value)
            value = template.render(field=field, player=player, statements=statements)
        except jinja2.exceptions.TemplateSyntaxError as e:

            print_error(f"     -- Unable to parse template from {block_type}: ", e.message, field, value)

    if not value:
        value = block_type
        print_error(f"     -- No BLOCK_MAPPING found for key '{block_type}', using key as value: '{value}'")

    return value


def generate_toolbox_python(root, player="player"):
    toolbox_blocks_element: ET.Element = root.find("./blocks/toolbox_blocks/xml")
    code = ["Here are elements from the toolbox.\nYou can use them in your code:", "```"]
    if toolbox_blocks_element:
        for block_element in toolbox_blocks_element:
            code.append(block_to_code(block_element, player))

    code.append("```")

    return "\n".join(code)


def generate_python_from_blocks(toolbox_blocks_element: ET.Element, player="player", indent=0) -> str:
    code = []

    if toolbox_blocks_element:
        for block_element in toolbox_blocks_element:
            code.append(block_to_code(block_element, player))

    code = "\n".join(code)
    if indent > 0:
        code = textwrap.indent(code, ' '*indent)

    return code


def block_to_code(block_element, player):
    field = {}
    statements = {}
    block_type = block_element.attrib.get("type")
    limit = block_element.attrib.get("limit")

    next_elem = None

    for child in block_element:
        if child.tag in ["title", "field"]:
            name = child.attrib.get("name")
            if name:
                field[name] = map_field(block_type, child.text, player=player)
        elif child.tag == "statement":
            name = child.attrib.get("name")
            if name:
                statements[name] = generate_python_from_blocks(child, player, 4)
        elif child.tag == "next":
            next_elem = child

    codeline = map_block(block_type, field, player, statements)

    if next_elem:
        next_code = generate_python_from_blocks(next_elem, player, 0)
        codeline = "\n".join([codeline, next_code])

    print(f"--- block_to_code({block_element}, {player}):")
    print(codeline)
    print('---')
    return codeline

