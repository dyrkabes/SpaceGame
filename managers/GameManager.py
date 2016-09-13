import Constants


class GameManager:
    """
    Probably not the class you could think about looking at it's name
    For now it just stores state - like paused/unpaused (running atm)
    """
    def __init__(self):
        self.state = Constants.StateConstants.WAITING
        self.cycles_past = 0

    def switch_running(self):
        if self.get_state() == Constants.StateConstants.WAITING:
            self.state = Constants.StateConstants.RUNNING
            self.cycles_past = 0
        else:
            self.state = Constants.StateConstants.WAITING

    def increase_cycles_past(self):
        self.cycles_past += 1
        if self.cycles_past == 10000:
            self.cycles_past = 0
            self.state = Constants.StateConstants.WAITING

    def get_state(self):
        return self.state
