"""automactic door system using state pattern
"""
from abc import ABC, abstractmethod


class State(ABC):
    """State Abstract Class
    """

    @abstractmethod
    def action(self):
        """change state with do any action
        """


class OpenState(State):
    """Open State
    """

    def action(self):
        print("The door opened.")


class CloseState(State):
    """Close State
    """

    def action(self):
        print("The door closed.")


class DoorManagement(State):
    """Automatic door management."""

    def __init__(self):
        self.state: State = None

    def get_state(self):
        """get door state
        """
        return self.state

    def set_state(self, state: State):
        """set door state

        Args:
            state (State): state of door
        """
        self.state = state

    def action(self):
        self.state.action()


if __name__ == "__main__":
    context = DoorManagement()
    open_state = OpenState()
    close_state = CloseState()
    context.set_state(open_state)
    context.action()
    context.set_state(close_state)
    context.action()
    context.action()
