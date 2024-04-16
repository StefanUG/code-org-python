import xml.etree.ElementTree as ET
import jinja2
import textwrap
import sys
import re


def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def sanitize_methodname(name):
    name = re.sub(r'[\\/*?:\"<>|]', "_", name)
    name = name.replace(" ", "_")
    return name

# Define the mapping from XML block types to Python constructs
BLOCK_MAPPING = {
    # Generally applicable blocks
    "when_run": "# Start",
    "controls_repeat":      "for i in range({{field['TIMES']}}):\n{{statements['DO']}}",
    "controls_repeat_ext":  "for i in range({{statements['TIMES']}}):\n{{statements['DO']}}",
    "controls_for":         "for {{field['VAR']}} in range({{statements['FROM']}}, {{statements['TO']}}, {{statements['BY']}}):\n{{statements['DO']}}",
    "math_arithmetic":  "{{statements['A']}}{{field['OP']}}{{statements['B']}}",
    "math_number":      "{{field['NUM']}}",
    "parameters_get":   "{{field['VAR']}}",
    "variables_set":    "{{field['VAR']}} = {{statements['VALUE']}}",
    "variables_get":    "{{field['VAR']}}",

    "comment": "# {{field['TEXT']}}",

    "procedures_defnoreturn": "def {{ sanitize_methodname(field['NAME']) }}({{mutation['args']}}):\n{{statements['STACK']}}\n\n",
    "procedures_callnoreturn": "{{ mutation['name'] }}({{mutation['args']}})",

    # Generic Maze blocks
    "maze_untilBlockedOrNotClear": "while {{field['DIR']}}:\n{{statements['DO']}}",
    "maze_moveForward":  "{{player}}.forward()",
    "maze_turn":         "{{player}}.{{field['DIR']}}",
    "maze_untilBlocked": "while {{player}}.path_ahead():\n{{statements['DO']}}",
    "maze_move":         "{{player}}.{{field['DIR']}}",
    "maze_ifElse":       "if {{player}}.{{field['DIR']}}:\n{{statements['DO']}}\nelse:\n{{statements['ELSE']}}",
    "maze_if":           "if {{player}}.{{field['DIR']}}:\n{{statements['DO']}}",
    "maze_forever":      "while not {{player}}.at_finish():\n{{statements['DO']}}",

    # Farmer related
    "maze_fill": "{{player}}.fill()",
    "maze_dig":  "{{player}}.remove()",

    # Harverster related
    "harvester_corn":    "{{player}}.pick_corn()",
    "harvester_lettuce": "{{player}}.pick_lettuce()",
    "harvester_pumpkin": "{{player}}.pick_pumpkin()",
    "harvester_whileHasCrop":    "while {{player}}.{{field['LOC']}}:\n{{statements['DO']}}",
    "harvester_untilHasCrop":    "while not {{player}}.{{field['LOC']}}:\n{{statements['DO']}}",
    "harvester_untilHasPumpkin": "while not {{player}}.at_pumpkin():\n{{statements['DO']}}",
    "harvester_ifHasCropElse":   "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}\nelse:\n{{statements['ELSE']}}",
    "harvester_ifHasCrop":       "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}",

    # Bee related
    "maze_honey":  "{{player}}.make_honey()",
    "maze_nectar": "{{player}}.get_nectar()",
    "bee_whileNectarAmount": "while {{field['ARG1']}} {{field['OP']}} {{field['ARG2']}}:\n{{statements['DO']}}",
    "bee_ifFlower":     "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}",
    "bee_ifElseFlower": "if {{player}}.{{field['LOC']}}:\n{{statements['DO']}}\nelse:\n{{statements['ELSE']}}",

    "collector_collect": "{{player}}.collect()"
}
# Aliases
BLOCK_MAPPING["controls_repeat_dropdown"] = BLOCK_MAPPING['controls_repeat']

FIELD_MAPPING = {
    "math_arithmetic/ADD":      "+",
    "math_arithmetic/MINUS":    "-",
    "math_arithmetic/MULTIPLY": "*",
    "math_arithmetic/DIVIDE":   "/",
    "math_arithmetic/POWER":    "^",

    # Generic Maze blocks
    "maze_turn/turnRight":    "right()",
    "maze_turn/turnLeft":     "left()",
    "maze_move/moveForward":  "forward()",
    "maze_move/moveBackward": "backward()",

    "maze_if/isPathForward":     "path_ahead()",
    "maze_if/isPathLeft":        "path_left()",
    "maze_if/isPathRight":       "path_right()",

    "maze_ifElse/isPathForward": "path_ahead()",
    "maze_ifElse/isPathLeft":    "path_left()",
    "maze_ifElse/isPathRight":   "path_left()",

    "maze_untilBlockedOrNotClear/holePresent":   "{{player}}.at_hole()",
    "maze_untilBlockedOrNotClear/pilePresent":   "{{player}}.at_pile()",
    "maze_untilBlockedOrNotClear/isPathForward": "{{player}}.path_ahead()",

    "harvester_whileHasCrop/Corn":    "has_corn()",
    "harvester_whileHasCrop/Pumpkin": "has_pumpkin()",
    "harvester_whileHasCrop/Lettuce": "has_lettuce()",
    "harvester_untilHasCrop/Corn":    "has_corn()",
    "harvester_untilHasCrop/Pumpkin": "has_pumpkin()",
    "harvester_untilHasCrop/Lettuce": "has_lettuce()",

    "harvester_ifHasCropElse/Corn":    "has_corn()",
    "harvester_ifHasCropElse/Pumpkin": "has_pumpkin()",
    "harvester_ifHasCropElse/Lettuce": "has_lettuce()",
    "harvester_ifHasCrop/Corn":        "has_corn()",
    "harvester_ifHasCrop/Pumpkin":     "has_pumpkin()",
    "harvester_ifHasCrop/Lettuce":     "has_lettuce()",

    "bee_whileNectarAmount/nectarRemaining": "{{player}}.nectar()",
    "bee_whileNectarAmount/honeyAvailable":  "{{player}}.honey()",
    "bee_whileNectarAmount/>": ">",
    "bee_whileNectarAmount/<": "<",
    "bee_whileNectarAmount/=": "==",

    "bee_ifFlower/atFlower":        "at_flower()",
    "bee_ifFlower/atHoneycomb":     "at_honeycomb()",
    "bee_ifElseFlower/atFlower":    "at_flower()",
    "bee_ifElseFlower/atHoneycomb": "at_honeycomb()",
}

J2_ENVIRONMENT = jinja2.Environment()
J2_ENVIRONMENT.globals['sanitize_methodname'] = sanitize_methodname
J2_ENVIRONMENT.globals['BLOCK_MAPPING'] = BLOCK_MAPPING
J2_ENVIRONMENT.globals['FIELD_MAPPING'] = FIELD_MAPPING

def map_field(block_type, text, player):
    key = f"{block_type}/{text}"
    value = FIELD_MAPPING.get(key)
    if value:
        template = J2_ENVIRONMENT.from_string(value)
        value = template.render(player=player)
    else:
        if text is None:
            text = ""
        value = text
        print(f"     -- No FIELD_MAPPING found for key '{key}', using value from attribute '{value}'")

    return value


def map_block(block_type, field, player, statements=None, mutation=None) -> str:
    value = BLOCK_MAPPING.get(block_type)
    if not statements:
        statements = {"DO": "    # Do this", "ELSE": "    # Otherwise this"}
    if value:
        try:
            template = J2_ENVIRONMENT.from_string(value)
            value = template.render(field=field, player=player, statements=statements, mutation=mutation)
        except jinja2.exceptions.TemplateSyntaxError as e:

            print_error(f"     -- Unable to parse template from {block_type}: ", e.message, field, value)

    if not value:
        value = block_type
        print_error(f"     -- No BLOCK_MAPPING found for key '{block_type}', using key as value: '{value}'")

    return value


def generate_toolbox_python(root, player="player", skip_wording=False):
    if type(root) is ET.ElementTree:
        toolbox_blocks_element: ET.Element = root.find("./blocks/toolbox_blocks/xml")
    else:
        toolbox_blocks_element = root

    code = [] if skip_wording else ["Here are elements from the toolbox.\nYou can use them in your code:", "```"]
    if toolbox_blocks_element:
        for block_element in toolbox_blocks_element:
            if block_element.tag == "category":
                code.append(f"\n#\n# {block_element.attrib.get('name')}\n")
                code.append(generate_toolbox_python(block_element, player, skip_wording=True))
            else:
                code.append(block_to_code(block_element, player))

    if not skip_wording:
        code.append("```")

    return "\n".join(code)


def generate_python_from_blocks(blocks_element: ET.Element, player="player", indent=0) -> str:
    when_run = None
    code = []

    if blocks_element:
        for block_element in blocks_element:
            block_type = block_element.attrib.get("type")
            generated_code = block_to_code(block_element, player)
            if block_type == "when_run":
                # When Run needs to be the last thing to run,
                # so we save it for last, so it can be inserted first - at the end.
                # In Python the functions need to be defined before they can be called.
                when_run = generated_code
            elif block_type == "procedures_defnoreturn":
                # When a function is defined, insert it first
                code.insert(0, generated_code)
            else:
                code.append(generated_code)

    if when_run:
        # At last, append the when_run element
        code.append(when_run)

    code = "\n".join(code)
    if indent > 0:
        code = textwrap.indent(code, ' '*indent)

    return code


def controls_for_workaround(statements):
    start = statements.get("FROM")
    if start is None:
        start = 0
    stop = statements.get("TO")
    if stop is None:
        stop = 1
    else:
        if "/" in stop:
            stop = f"int({stop})"
    step = statements.get("BY")
    if step is None:
        step = 1

    try:
        start = int(start)
        stop = int(stop)
        step = int(step)

        if start > stop: # Counting down
            step = step * -1

        stop = stop + step
    except ValueError:
        stop = stop + "+1"


    statements["TO"] = stop
    statements["BY"] = step


def block_to_code(block_element, player):
    field = {}
    statements = {}
    mutation = {}
    block_type = block_element.attrib.get("type")
    limit = block_element.attrib.get("limit")

    next_elem = None

    for child in block_element:
        if child.tag in ["title", "field"]:
            # When it is a literal value / field
            name = child.attrib.get("name")
            if name:
                field[name] = map_field(block_type, child.text, player=player)
        elif child.tag in ["statement", "value"]:
            # When it is code that needs to be generated
            name = child.attrib.get("name")
            if name:
                statements[name] = generate_python_from_blocks(child, player, 4)
                if child.tag == "value":
                    # When it's a value, it is used in a conditional and needs to be stripped
                    statements[name] = statements[name].strip()
        elif child.tag == "mutation":
            name = child.attrib.get("name")
            if name:
                mutation['name'] = sanitize_methodname(name)

            args = []
            for mute in child:
                # E.g.
                # <mutation>
                #     <arg name="length"/>
                # </mutation>
                if mute.tag == "arg":
                    args.append(mute.attrib.get("name"))
            if len(args) > 0:
                mutation['args'] = args

        elif child.tag == "next":
            next_elem = child

    #
    # METHOD DEF and CALL SECTION
    #
    # Preparing the arguments, either in the definition or the values to be passed

    if mutation.get('name') and mutation.get('args'):
        # Assume it is a method call that needs the value of the args passed
        values = []
        for i in range(len(mutation['args'])):
            value = statements.get('ARG'+str(i))
            if value is None:
                value = "?"
            values.append(f"{mutation['args'][i]}={value}")
        mutation['args'] = ", ".join(values)
    elif mutation.get('args'):
        mutation['args'] = ", ".join(mutation['args'])
    else:
        mutation['args'] = ""

    #
    # WORKAROUND SECTION
    #

    if block_type == "controls_for":
        # Workaround for counting down in range, not working like `range` is designed
        controls_for_workaround(statements)
    elif block_type == "controls_repeat_ext":
        # workaround to the fact that a python division results in a float, which fails in `range`
        times = statements.get("TIMES")
        if times and "/" in times:
            times = f"int({times})"
            statements["TIMES"] = times


    codeline = map_block(block_type, field, player, statements, mutation)

    if limit:
        lines = codeline.split("\n")
        lines[0] += f" # limit: {limit}"
        codeline = "\n".join(lines)

    if next_elem:
        next_code = generate_python_from_blocks(next_elem, player, 0)
        codeline = "\n".join([codeline, next_code])

    return codeline

