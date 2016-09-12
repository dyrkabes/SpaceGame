from Constants import ShipConstants
from shipComponents.Component import Component


class Shell(Component):
    def __init__(self, ship):
        Component.__init__(self, ShipConstants.SHELL, ship)
        self.hitpoints = 450
        self.name = ShipConstants.SHELL

    def get_hitpoints(self):
        return self.hitpoints

    def decrease_hitpoints(self, damage):
        self.hitpoints -= damage
        if self.hitpoints <= 0:
            self.state_manager.new_message("Destroyed")

    def get_damage(self, damage):
        print("MESSAGE: SHELL special effects")

    def load_modules(self):
        pass
