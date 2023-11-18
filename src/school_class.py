import random
from typing import List

from src.group import Group
from src.pupil import Pupil


class SchoolClass:
    def __init__(self, name: str):
        self._name = name
        self._pupils: List[Pupil] = self.load_pupils()

    @property
    def name(self) -> str:
        return self._name

    @property
    def pupils(self) -> List[Pupil]:
        return self._pupils

    @classmethod
    def instantiate(cls, name: str):
        return cls(name)

    def load_pupils(self) -> List[Pupil]:
        # todo: Check if file exists
        with open(f"school_classes/{self.name}.txt", "r") as file:
            return [Pupil(line.rstrip()) for line in file]

    def draw_pupil(self, only_healthy=True) -> str:
        pupils = self.pupils
        if only_healthy:
            pupils = self.get_healthy_pupils()

        pupil = random.choice(pupils)
        return pupil.name

    def get_healthy_pupils(self) -> List[Pupil]:
        return [pupil for pupil in self.pupils if not pupil.is_sick]

    def split_into_n_groups(self, n: int, group_names: str = None, only_healthy: bool = True) -> List[Group]:
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
            group_name = str(i+1) if not group_names else str(group_names[i])
            group = Group(group_name, pupils)
            groups.append(group)
            start += group_size

        for idx, pupil in enumerate(all_pupils[end:]):
            current_group = groups[idx]
            current_group.add_pupil(pupil)

        return groups
