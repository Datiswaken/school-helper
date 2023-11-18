import argparse
from typing import List

from src.school_class import SchoolClass

SICK_PUPILS = "Please mark any sick pupils. Just press ENTER if no pupils are sick.\n"
ONLY_HEALTHY = "Should sick pupils be considered? yes/no\n"
ACTION_INPUT = "Choose an action:\n(1): Draw a random pupil\n(2): Split pupils into groups\n"
N = "How many groups should the pupils be split into?\n"
GROUP_NAMES = ("You can specify group names. If you skip this step groups will be number 1 to N. Names must be "
               "separated by commas. To skip just press ENTER.\n")


def mark_sick_pupils(school_class: SchoolClass, pupil_names: List[str]) -> None:
    for pupil in school_class.pupils:
        for name in pupil_names:
            if pupil.name == name:
                pupil.is_sick = True


def run(school_class_name: str):
    school_class = SchoolClass.instantiate(school_class_name)
    sick_pupils = input(SICK_PUPILS)
    sick_pupils = sick_pupils if sick_pupils != "" else None
    only_healthy = None
    if sick_pupils:
        sick_pupils = sick_pupils.split(",")
        sick_pupils = [name.strip() for name in sick_pupils]
        mark_sick_pupils(school_class, sick_pupils)

        while type(only_healthy) is not bool:
            only_healthy_input = input(ONLY_HEALTHY)
            if only_healthy_input.lower() == "yes":
                only_healthy = True
            elif only_healthy_input.lower() == "no":
                only_healthy = False
            else:
                print("Please choose either 'yes' or 'no'")

    if not only_healthy:
        only_healthy = True
    action = input(ACTION_INPUT)
    if action == "1":
        print(f"Randomly drawn pupil is {school_class.draw_pupil(only_healthy=only_healthy)}")
    elif action == "2":
        number_of_groups = int(input(N))
        group_names = input(GROUP_NAMES)
        group_names = group_names if group_names != "" else None
        for group in school_class.split_into_n_groups(
                n=number_of_groups,
                group_names=group_names,
                only_healthy=only_healthy
        ):
            print(group)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("school_class", type=str, help="A school class, e.g. 5d")
    args = parser.parse_args()
    school_class_name = args.school_class
    run(school_class_name=school_class_name)
