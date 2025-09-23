import xml.etree.ElementTree as ET
import json
import argparse
import os
import shutil

import jinja2

from .code_blocks import generate_toolbox_python, generate_python_from_blocks


def create_levels_json(levelfiles: list, target_dir):
    if isinstance(levelfiles, str):
        levelfiles = [levelfiles]

    loaded_json = []

    for levelfile in levelfiles:
        try:
            print("creating level for", levelfile)
            root = ET.parse(levelfile)
            loaded_json.append(extract_level_json(levelfile, root, target_dir))
        except (AttributeError, KeyError) as err:
            print(f"Error handling file: {levelfile} : ", err)

    return loaded_json


def extract_level_json(levelfile, root, target_dir):
    # Find the 'config' node and extract the JSON data
    config_node = root.find('config')
    json_data = config_node.text

    # Load the JSON data as a Python dictionary
    data = json.loads(json_data)

    filename = os.path.basename(levelfile)
    filename = os.path.splitext(filename)[0]
    filename = f"{target_dir}/{filename}.json"

    # Save the Python dictionary as a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f" -- Saved json to '{filename}'")

    return data


# Get the directory of the current Python file
_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

SKIN_PLAYER = {
    # '[SKIN NAME]', ('[VARIABLE NAME IN PY]', '[CLASS NAME IN PY]')
    'pvz': ('zombie', 'ZombiePlayer'),
    'harvester': ('farmer', 'Harvester'),
    'farmer': ('farmer', 'Farmer'),
    'bee': ('bee', 'BeePlayer'),
    'birds': ('bird', 'Bird'),
    'collector': ('collector', 'Collector')
}


def create_maze_python(level_filename: str, level_key, course, lesson, level, level_xml):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(_DIR_PATH))
    skin = level['config']['properties'].get('skin')

    contained_levels = level['config']['properties'].get("contained_level_names")

    mapping = SKIN_PLAYER.get(skin)
    if mapping:
        (player, player_type) = mapping
    else:
        print(f" -- No player mapping found for {skin}")
        return

    template = environment.get_template(f"maze.py.j2")
    toolbox = generate_toolbox_python(level_xml, player)
    start_code = generate_python_from_blocks(level_xml.find("./blocks/start_blocks/xml"), player)
    solution_code = generate_python_from_blocks(level_xml.find("./blocks/solution_blocks/xml"), player)

    # Create the level / puzzle file
    content = template.render(course=course, lesson=lesson, level=level, levelname=level_key, toolbox=toolbox,
                              player=player, player_type=player_type, start_code=start_code)

    with open(f"{level_filename}.py", mode="w", encoding="utf-8") as file:
        file.write(content)

    # Create the solution / test file
    content = template.render(course=course, lesson=lesson, level=level, levelname=level_key, toolbox=toolbox,
                              player=player, player_type=player_type, start_code=solution_code)

    filename = os.path.basename(level_filename)
    filename = level_filename.replace(filename, "levels/test_" + filename)

    with open(f"{filename}.py", mode="w", encoding="utf-8") as file:
        file.write(content)

    # create a test_all.py file, if one does not exist
    dirname = os.path.dirname(filename)
    test_all_file = os.path.join(dirname, "test_all.py")
    print("test all file", test_all_file, "exist?", os.path.exists(test_all_file))
    if not os.path.exists(test_all_file):
        print("Copy test_all.py to ", test_all_file)
        shutil.copy(os.path.join(_DIR_PATH, "test_all.py"), test_all_file)

    print(f" -- wrote level to {level_filename}.py")


def handle_level(levelfile, leveltype, levels_dirname, level_filename, level_key, course, lesson, level):
    """

    :param levelfile: the source level file, typically a `.level`
    :param leveltype: e.g. maze
    :param levels_dirname: the target directory to store the levels in
    :param level_filename: the target filename without extension, including directory
    :param level_key: the name of the level, which is also the key, e.g. "While Loops in Farmer"
    :param course: the course json
    :param lesson: the lesson json
    :param level: the level json
    :return:
    """
    print("HANDLE LEVEL: ", os.path.basename(levelfile), "type:", leveltype, "target:", level_filename)
    os.makedirs(levels_dirname, exist_ok=True)

    # Load the level XML
    root = ET.parse(levelfile)

    # Extract the JSON, and store that
    level_config = extract_level_json(levelfile, root, levels_dirname)
    level['config'] = level_config

    # Generate the level python, including the toolbox code
    create_maze_python(level_filename, level_key, course, lesson, level, root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Level importer/converter',
        description='Import a level file from code-dot-org and store it locally to the',
        epilog='Text at the bottom of help')

    parser.add_argument('levelfile', nargs='+',
                        help='The file of the level to import and convert')

    parser.add_argument('-t', '--target_dir', default="levels/", required=False,
                        help='Target directory to store the converted files')

    args = parser.parse_args()

    create_levels_json(args.levelfile, args.target_dir)
