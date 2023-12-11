class UserInput:
    def __init__(self, input_request: str, options: list[str] = None, skippable: bool = False, default: str = None):
        self._input_request = input_request
        self._options = options
        self._user_input = ""
        self._valid = False
        self._skippable = skippable
        self._default = default

        if self._options and self._skippable:
            assert self._default is not None, ("A skippable user input with options must set one of those options as "
                                               "default.")
        elif self._skippable:
            assert self._default is not None, "A skippable user input must have a default value."

    @property
    def input_request(self) -> str:
        return self._input_request

    @property
    def options(self) -> list[str]:
        return self._options

    @property
    def user_input(self) -> str:
        return self._user_input

    @user_input.setter
    def user_input(self, value) -> None:
        self._user_input = value

    @property
    def valid(self) -> bool:
        return self._valid

    @valid.setter
    def valid(self, value) -> None:
        self._valid = value

    @property
    def skippable(self) -> bool:
        return self._skippable

    @property
    def default(self) -> str:
        return self._default

    def request_user_input(self):
        while not self._valid:
            self.user_input = input(self.input_request).strip().lower()
            if self.options:
                if self.user_input in map(str.lower, self.options):
                    self.valid = True
                    return self.user_input
                elif self.skippable and self.user_input == "":
                    self.valid = True
                    return self.default
            elif self.skippable:
                self.valid = True
                return self.default
            elif self.user_input != "":
                self.valid = True
                return self.user_input

            if self.options:
                print(f"Please choose on of {self.options}.")
            else:
                print(f"Your input may not be empty.")

    def skipped(self) -> bool:
        return self.user_input == ""
