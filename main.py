from typing import List

from src.school_class import SchoolClass
from src.setup.user_input import UserInput
from src.util.school_classes import get_school_class_names

YES = "yes"
NO = "no"

SCHOOL_CLASS_QUESTION = "Please choose a class: "
SICK_PUPILS_QUESTION = "Are there any sick pupils? yes/no. Default: no."
SICK_PUPILS = "Please name any sick pupils.\n"
ONLY_HEALTHY = "Should sick pupils be considered? yes/no. Default: no\n"
ACTION_INPUT = ("Choose an action:\n(1): Draw a random pupil\n(2): Split pupils into groups\n(3): Make groups of N "
                "pupils\n")
DRAW_RND_ACTION = "1"
SPLIT_INTO_GROUPS_ACTION = "2"
NUMBER_OF_GROUPS = "How many groups should the pupils be split into? "
GROUP_NAMES = ("You can specify group names. If you skip this step groups will be number 1 to N. Names must be "
               "separated by commas. To skip just press ENTER.\n")
NUMBER_OF_PUPILS_PER_GROUP = "How many pupils should each group consist of? "
MAKE_GROUPS_OF_N_ACTION = "3"
NEW_ACTION = "Press enter to choose a new action or press 'q' to quit. "


def mark_sick_pupils(school_class: SchoolClass, pupil_names: List[str]) -> None:
    for pupil in school_class.pupils:
        for name in pupil_names:
            if pupil.name == name:
                pupil.is_sick = True


def run():
    school_class_name_options = get_school_class_names()
    school_class_name = UserInput(
        input_request=SCHOOL_CLASS_QUESTION,
        options=school_class_name_options,
    ).request_user_input()
    school_class = SchoolClass.instantiate(school_class_name)
    only_healthy = True
    sick_pupils_question = UserInput(
        input_request=SICK_PUPILS_QUESTION,
        options=[YES, NO],
        skippable=True,
        default=NO
    ).request_user_input()
    if sick_pupils_question is not NO:
        sick_pupils = UserInput(
            input_request=SICK_PUPILS
        ).request_user_input()
        if sick_pupils:
            sick_pupils = sick_pupils.split(",")
            sick_pupils = [name.strip() for name in sick_pupils]
            school_class.mark_pupils_as_sick(sick_pupils)

            consider_sick_pupils = UserInput(
                input_request=ONLY_HEALTHY,
                options=[YES, NO],
                skippable=True,
                default=NO
            ).request_user_input()
            if consider_sick_pupils == YES:
                only_healthy = False

    exit_script = False
    while not exit_script:
        action = UserInput(
            input_request=ACTION_INPUT,
            options=["1", "2", "3"],
        ).request_user_input()
        if action == DRAW_RND_ACTION:
            pupil = school_class.draw_pupil(only_healthy=only_healthy)
            print(f"Randomly drawn pupil is {pupil.name}")
        elif action == SPLIT_INTO_GROUPS_ACTION:
            number_of_groups = int(input(NUMBER_OF_GROUPS))
            group_names = input(GROUP_NAMES)
            group_names = group_names if group_names != "" else None
            for group in school_class.split_into_n_groups(
                    n=number_of_groups,
                    group_names=group_names,
                    only_healthy=only_healthy
            ):
                print(group)
        elif action == MAKE_GROUPS_OF_N_ACTION:
            number_of_pupils_per_group = int(input(NUMBER_OF_PUPILS_PER_GROUP))
            for group in school_class.make_groups_of_n_pupils(n=number_of_pupils_per_group, only_healthy=only_healthy):
                print(group)

        new_action = UserInput(NEW_ACTION, options=["ENTER", "q"], skippable=True, default="new_action").request_user_input()
        if new_action == "q":
            exit_script = True


if __name__ == '__main__':
    run()
