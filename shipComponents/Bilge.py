from Constants import ShipConstants
from shipComponents.Component import Component


class Bilge(Component):
    def __init__(self, ship):
        Component.__init__(self, ShipConstants.BILGE, ship)
        self.name = ShipConstants.BILGE
        self.space_max = 50
        self.space = 0
        self.objects = []
        self.hitpoints = 1

    def get_free_space(self):
        return self.space_max - self.space

    def fill_bilge(self, object):
        self.objects.append(object)
        self.space += object.weight


    def get_damage(self, damage):
        Component.get_damage(self, damage)
        print("MESSAGE: bilge")

    def load_modules(self):
        pass
