"""mobile state management system using state pattern
"""


class State:
    """state class for type hint
    """
    name = 'null'
    allowed = []

    def switch(self):
        """switch to any state
        """

    def add_allowed(self):
        """add state to allowed list
        """


class MobileState:
    """mobile state class
    """
    name = 'state'
    allowed = []

    def switch(self, state: State):
        """switch to `state` if state is allowed

        Args:
            state (State): state of mobile
        """
        if state.name in self.allowed:
            print(f'Change "{self}" state to "{state.name}"')
            self.__class__ = state  # class change to `state`
        else:
            print(f'Impossible Change "{self}" to "{state.name}" state!')

    @classmethod
    def add_allowed(cls, state_name: str):
        """add state to allowed list

        Args:
            state_name (str): state name
        """
        cls.allowed.append(state_name)

    def __str__(self):
        return self.name


class Off(MobileState):
    """Mobile Off Mode
    """
    name = "Off"
    allowed = ['On']


class On(MobileState):
    """Mobile On Mode
    """
    name = "On"
    allowed = ['Off', 'Restart', 'Airplane']


class Restart(MobileState):
    """Mobile Restart Mode
    """
    name = "Restart"
    allowed = ['On']


class Airplane(MobileState):
    """Mobile Airplane Mode
    """
    name = "Airplane"
    allowed = ['On', 'Off', 'Restart']


class MobileManagement:
    """mobile management class
    """

    def __init__(self, model='SAMSUNG'):
        self.model = model
        # default state
        self.state = Off()

    def change(self, state: MobileState):
        """change mobile state to `state`

        Args:
            state (MobileState): new mobile state
        """
        self.state.switch(state)

    def get_state(self) -> str:
        """get current mobile state

        Returns:
            str: mobile state
        """
        return self.state.name


if __name__ == "__main__":
    mobile = MobileManagement()
    mobile.change(On)
    mobile.change(Off)
    mobile.change(Restart)
    mobile.change(On)
    mobile.change(Restart)
    mobile.change(On)
    mobile.change(Airplane)
    Off.add_allowed("Restart")
    mobile.change(Off)
    mobile.change(Restart)
    print("Current State is", mobile.get_state())
