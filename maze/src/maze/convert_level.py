import xml.etree.ElementTree as ET
import json
import argparse
import os

parser = argparse.ArgumentParser(
            prog='Level importer/converter',
            description='Import a level file from code-dot-org and store it locally to the',
            epilog='Text at the bottom of help')


parser.add_argument('levelfile', nargs='+',
                    help='The file of the level to import and convert')

parser.add_argument('-t', '--target_dir', default="levels/", required=False,
                    help='Target directory to store the converted files')

args = parser.parse_args()


for levelfile in args.levelfile:
  try:
    root = ET.parse(levelfile)

    # Find the 'config' node and extract the JSON data
    config_node = root.find('config')
    json_data = config_node.text

    # Load the JSON data as a Python dictionary
    data = json.loads(json_data)
    data["parsed_maze"] = json.loads(data["properties"]["serialized_maze"])

    filename = os.path.basename(levelfile)
    filename = os.path.splitext(filename)[0]
    filename = f"{args.target_dir}/{filename}.json"

    # Save the Python dictionary as a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Saved level to '{filename}'")
  except (AttributeError,KeyError) as err:
    print(f"Error with file: {levelfile}.", err)