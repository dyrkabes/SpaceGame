import Constants


class GameManager:
    """
    Probably not the class you could think about looking at it's name
    For now it just stores state - like paused/unpaused (running atm)
    """
    # TODO: probably I should make it's like a "State" pattern
    def __init__(self):
        self.pause_state = Constants.StateConstants.WAITING
        self.enviroment_state = Constants.StateConstants.OUTER_SPACE
        self.cycles_past = 0
        self.observers = []

    def switch_running(self):
        if self.get_state() == Constants.StateConstants.WAITING:
            self.pause_state = Constants.StateConstants.RUNNING
            self.cycles_past = 0
        else:
            self.pause_state = Constants.StateConstants.WAITING

    def change_enviroment(self, new_state):
        self.enviroment_state = new_state
        self.notify_enviroment_state_observers()

    def increase_cycles_past(self):
        self.cycles_past += 1
        if self.cycles_past == 10000:
            self.cycles_past = 0
            self.pause_state = Constants.StateConstants.WAITING

    def get_state(self):
        return self.pause_state

    def register_enviroment_state_observer(self, call_observer):
        self.observers.append(call_observer)

    def notify_enviroment_state_observers(self):
        for call_observer in self.observers:
            call_observer()
