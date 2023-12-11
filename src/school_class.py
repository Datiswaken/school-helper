from __future__ import annotations
import random

from src.group import Group
from src.pupil import Pupil


class SchoolClass:
    def __init__(self, name: str):
        self._name = name
        self._pupils: list[Pupil] = self.load_pupils()

    @property
    def name(self) -> str:
        return self._name

    @property
    def pupils(self) -> list[Pupil]:
        return self._pupils

    @classmethod
    def instantiate(cls, name: str) -> SchoolClass:
        return cls(name)

    def load_pupils(self) -> list[Pupil]:
        # todo: Check if file exists
        with open(f"school_classes/{self.name}.txt", "r") as file:
            return [Pupil(line.rstrip()) for line in file]

    def draw_pupil(self, only_healthy=True) -> Pupil:
        pupils = self.pupils
        if only_healthy:
            pupils = self.get_healthy_pupils()

        pupil = random.choice(pupils)
        return pupil

    def get_healthy_pupils(self) -> list[Pupil]:
        return [pupil for pupil in self.pupils if not pupil.is_sick]

    def split_into_n_groups(self, n: int, group_names: str = None, only_healthy: bool = True) -> list[Group]:
        if group_names:
            group_names = group_names.replace(" ", "").split(",")
            assert n == len(group_names), "Number of group names must match number of groups"

        all_pupils = self.pupils
        if only_healthy:
            all_pupils = self.get_healthy_pupils().copy()
        random.shuffle(all_pupils)
        group_size = len(all_pupils) // n
        groups = []
        start = 0
        end = 0
        for i in range(n):
            end += group_size
            pupils = all_pupils[start:end]
            group_name = str(i + 1) if not group_names else str(group_names[i])
            group = Group(group_name, pupils)
            groups.append(group)
            start += group_size

        for idx, pupil in enumerate(all_pupils[end:]):
            current_group = groups[idx]
            current_group.add_pupil(pupil)

        return groups

    def make_groups_of_n_pupils(self, n: int, only_healthy: bool = True) -> list[Group]:
        all_pupils = self.pupils
        if only_healthy:
            all_pupils = self.get_healthy_pupils().copy()
        number_of_groups = len(all_pupils) // n
        groups = []
        start = 0
        end = 0
        for i in range(number_of_groups):
            end += n
            pupils = all_pupils[start:end]
            group = Group(str(i + 1), pupils)
            groups.append(group)
            start += n

        for idx, pupil in enumerate(all_pupils[end:]):
            current_group = groups[idx]
            current_group.add_pupil(pupil)

        return groups

    def mark_pupils_as_sick(self, pupil_names: list[str]) -> None:
        for pupil in self.pupils:
            for name in pupil_names:
                if pupil.name.lower() == name.lower():
                    pupil.is_sick = True
