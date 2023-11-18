class Pupil:
    def __init__(self, name):
        self._name = name
        self._is_sick = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_sick(self):
        return self._is_sick

    @is_sick.setter
    def is_sick(self, value: bool) -> None:
        self._is_sick = value
