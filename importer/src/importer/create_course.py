import xml.etree.ElementTree as ET
import json
import argparse
import os
from os.path import join as joinpaths
import re
import jinja2
from . import convert_level

# Get the directory of the current Python file
_dir_path = os.path.dirname(os.path.realpath(__file__))


def sanitize_filename(filename, replace_spaces=False):
    filename = re.sub(r'[\\/*?:\"<>|]', "-", filename)
    if replace_spaces:
        filename = filename.replace(" ", "_")
    return filename


# Defines the folders to look through
# TODO Support "turtle" and "flappy"
SUPPORTED_LEVEL_TYPES = [
    ("maze", joinpaths("levels", "custom", "maze"), "level"),
    ("unplug", joinpaths("levels", "custom", "unplug"), "level"),
    ("standalone_video", joinpaths("levels", "custom", "standalone_video"), "level"),
    ("external", "scripts", "external")
]


def find_level_file(levelname, startdir):
    dir_prefix = joinpaths("dashboard", "config")
    levelfile = f"{levelname}"

    for leveltype in SUPPORTED_LEVEL_TYPES:
        filename = joinpaths(startdir, dir_prefix, leveltype[1], levelfile + "." + leveltype[2])
        if os.path.exists(filename):
            return filename, leveltype[0]

    return None, None


def find_course_file(coursename, source_dir):
    return joinpaths(source_dir, "dashboard", "config", "scripts_json", coursename + ".script_json")


def create_level_python(level_filename, level_key, course, lesson, level):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(_dir_path))
    skin = level['config']['properties'].get('skin')
    if skin and skin in ['pvz', 'bee', 'farmer', 'harvester']:
        skin = "_" + skin
    else:
        skin = ""
    template = environment.get_template(f"maze{skin}.py.j2")
    content = template.render(course=course, lesson=lesson, level=level, levelname=level_key)
    with open(f"{level_filename}.py", mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"Wrote level to {level_filename}.py")

    #


# Structure of the code-dot-org course script is:
# - lesson_groups, e.g. High level "Loops" or "Conditionals"
# - lessons, e.g. "Nested Loops in Maze"
# - lesson_activities, e.g. "Warm up", "Main Activity", "Wrap Up"
# - activity_sections, e.g. "Skill Building", "Prediction"
# - script_levels, e.g. each level in skill building


#
#
# An lesson_activity looks like this, and is not needed to generate the puzzle files
#
#   "key": "8fe0f456-c4bd-4d50-bee3-fa311f5cc147",
#   "position": 1,
#   "properties": {
#     "duration": 10,
#     "name": "Warm Up"
#   },
#   "seeding_key": {
#     "lesson_activity.key": "8fe0f456-c4bd-4d50-bee3-fa311f5cc147",
#     "lesson.key": "Nested Loops in Maze",
#     "lesson_group.key": "csf_loops",
#     "script.name": "coursed-2023"
#   }
#
#
# An activity_section looks like this:
#  {
#    "key": "b9ae7539-4e07-42a1-a318-77b57bcebe7f",
#    "position": 1,
#    "properties": {
#      "description": "These puzzles might sprout some questions, so have the students work in pairs or implement the
#                     \"Ask three before you ask me\" rule (have the students ask three other peers for help before they
#                     go to the teacher.) This will spark discussions that will develop each student's understanding.",
#      "name": "If/Else with Bee"
#    },
#    "seeding_key": {
#      "activity_section.key": "b9ae7539-4e07-42a1-a318-77b57bcebe7f",
#      "lesson_activity.key": "293c782d-3e53-4092-bea7-c4ed864214b0"
#    }
#  },


# course file e.g. 
# code-dot-org/dashboard/config/scripts_json/coursed-2023.script_json
# code-dot-org/dashboard/config/levels/custom/maze/courseD_bee_conditionals3_2023.level


def generate_courses(coursename, source_dir, target_dir):
    coursefile = find_course_file(coursename, source_dir)
    with open(coursefile) as f:
        course = json.load(f)
        course['key'] = coursename

        lesson_group_seq = 0

        # A lesson_group looks like this:
        #
        #   "key": "csf_conditionals",
        #   "user_facing": true,
        #   "position": 5,
        #   "properties": {
        #     "display_name": "Conditionals"
        #   },
        #   "seeding_key": {
        #     "lesson_group.key": "csf_conditionals",
        #     "script.name": "coursed-2023"
        #   }
        for lesson_group in course.get("lesson_groups"):
            lesson_group_seq += 1

            # Get relevant properties from lesson_group
            group_name = lesson_group["properties"]["display_name"]
            lesson_group_key = lesson_group["key"]

            # Directory name for Group

            # A lesson looks like this:
            #
            #   "key": "If/Else with Bee",
            #   "name": "If/Else with Bee",
            #   "absolute_position": 14,
            #   "lockable": false,
            #   "has_lesson_plan": true,
            #   "relative_position": 14,
            #   "properties": {
            #     "creative_commons_license": "Creative Commons BY-NC-SA",
            #     "overview": "In this **skill-building** lesson, your class will continue to code with conditionals,
            #                 allowing them to write code that functions differently depending on the specific
            #                 conditions the program encounters.",
            #     "preparation": " - Play through the puzzles to find any potential problem areas for your class.\n",
            #     "purpose": "After being introduced to conditionals in \"Conditionals with Cards,\" students will now
            #                practice using them in their programs. The \"if / else\" blocks will allow for a more
            #                flexible program. The bee will only collect nectar *if* there is a flower or make honey
            #                *if* there is a honeycomb. ",
            #     "student_overview": "Now that you understand conditionals, it's time to program Bee to use them when
            #                         collecting honey and nectar. ",
            #     ["unplugged": true] # Only present when unplugged
            #   },
            #   "seeding_key": {
            #     "lesson.key": "If/Else with Bee",
            #     "lesson_group.key": "csf_conditionals",
            #     "script.name": "coursed-2023"
            #   }
            for lesson in course.get("lessons"):
                if lesson["seeding_key"]["lesson_group.key"] == lesson_group_key:

                    props = lesson["properties"]

                    cc_license = props.get("creative_commons_license")
                    lesson_seq = lesson["absolute_position"]
                    lesson_key = lesson["key"]
                    lesson_unplugged = bool(props.get("unplugged"))

                    lesson_name = lesson["name"]

                    # Only continue if the lesson is under Creative Commons license
                    if cc_license:

                        # Directory name for the lesson
                        course_dirname = f"{args.target_dir}/{lesson_group['seeding_key']['script.name']}"
                        lesson_dirname = sanitize_filename(f"{lesson_seq} - {group_name} - {lesson_key}")
                        lesson_dirname = f"{course_dirname}/{lesson_dirname}"
                        levels_dirname = f"{lesson_dirname}/levels"
                        os.makedirs(lesson_dirname, exist_ok=True)

                        # TODO Make Lesson MD file for the lesson

                        # A script_level looks like this:
                        #
                        #  "chapter": 120,
                        #  "position": 4,
                        #  "activity_section_position": 2,
                        #  "assessment": false,
                        #  "properties": {
                        #    "level_keys": [
                        #      "courseD_bee_conditionals3_2023"
                        #    ],
                        #    "progression": "Skill Building"
                        #  },
                        #  "bonus": false,
                        #  "seeding_key": {
                        #    "script_level.level_keys": [
                        #      "courseD_bee_conditionals3_2023"
                        #    ],
                        #    "lesson.key": "If/Else with Bee",
                        #    "lesson_group.key": "csf_conditionals",
                        #    "script.name": "coursed-2023",
                        #    "activity_section.key": "c3e5d3a5-f776-4bd6-93d6-821025f2c40f"
                        #  },
                        #  "level_keys": [
                        #    "courseD_bee_conditionals3_2023"
                        #  ]
                        for level in course.get("script_levels"):
                            props = level["properties"]
                            level_key = level["level_keys"][0]  # TODO, check if there could ever be more
                            level_seq = level["position"]
                            level_progression = props.get("progression")
                            section_pos = level["activity_section_position"]

                            if lesson_key == level["seeding_key"]["lesson.key"]:
                                if level_progression:
                                    level_progression = sanitize_filename(level_progression)
                                    level_filename = f"{lesson_dirname}/{level_seq}_{level_progression}_{section_pos}"
                                else:
                                    level_filename = f"{lesson_dirname}/{level_seq}_{section_pos}"

                                (levelfile, leveltype) = find_level_file(level_key, source_dir)
                                if not levelfile:
                                    print(f"No levefile foud for: {level_key}")
                                    continue

                                print("treating levelfile ", levelfile, leveltype)
                                if leveltype == 'maze':
                                    os.makedirs(levels_dirname, exist_ok=True)
                                    level_config = convert_level.create_level_json(levelfile, levels_dirname)
                                    level['config'] = level_config[0]
                                    create_level_python(level_filename, level_key, course, lesson, level)
                                elif leveltype == 'unplug':
                                    print("unplug levels not yet implemented")
                                elif leveltype == 'standalone_video':
                                    print("standalone_video levels not yet implemented")
                                elif leveltype == 'external':
                                    print("external levels not yet implemented")

                    else:
                        print(f"Skipping lesson '{lesson_name}' as it does not have a creative_commons_license")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Course importer/converter',
        description='Import a course file from code-dot-org and create empty puzzle files',
        epilog='example: \ncreate_course -s ../code-dot-org -t course/ coursed-2023')

    parser.add_argument('-s', '--source_dir',
                        help='The root folder for code-dot-org codebase, to look for courses within')

    parser.add_argument('-t', '--target_dir', default="course/", required=False,
                        help='Target directory to store the output files')

    parser.add_argument('coursename',
                        help='The name of the course to import and convert')

    args = parser.parse_args()

    generate_courses(args.coursename, args.source_dir, args.target_dir)
