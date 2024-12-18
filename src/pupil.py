from typing import Optional


class Pupil:
    def __init__(self, name, is_sick: Optional[bool] = False):
        self._name = name
        self._is_sick = is_sick

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_sick(self) -> bool:
        return self._is_sick

    @is_sick.setter
    def is_sick(self, value: bool) -> None:
        self._is_sick = value
