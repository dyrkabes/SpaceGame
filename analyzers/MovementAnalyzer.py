import random

class MovementAnalyzer:
    @staticmethod
    def get_destination(ship):
        if not ship.x_movement_speed and not ship.y_movement_speed and not ship.player_ship:
            ship.x_destination = random.randint(-5, 200)
            ship.y_destination = random.randint(-5, 200)