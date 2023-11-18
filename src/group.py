from typing import List, Union

from src.pupil import Pupil


class Group:
    def __init__(self, name: str, pupils: List[Pupil]):
        self._name = name
        self._pupils = pupils
        self._size = len(self._pupils)

    def __repr__(self) -> str:
        member_names = [pupil.name for pupil in self.pupils]
        output = f"""Group name: {self.name}\nGroup size: {self.size}\nGroup members: """
        for name in member_names[:-1]:
            output += f"{name}, "
        output += f"{member_names[-1]}\n"

        return output

    @property
    def name(self) -> str:
        return self._name

    @property
    def pupils(self) -> List[Pupil]:
        return self._pupils

    @property
    def size(self) -> int:
        return self._size

    def add_pupil(self, pupil: Pupil) -> None:
        self._pupils.append(pupil)
        self._size += 1
