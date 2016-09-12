import math

class GravityManager:
    @staticmethod
    def apply_gravity_effects(entity, star):
        x_gravity_effect, y_gravity_effect  = GravityManager.calc_gravity_effects(entity, star)
        entity.change_movement_speed(x_gravity_effect, y_gravity_effect)
        pass

    @staticmethod
    def calc_gravity_effects(entity, star):
        x_delta = entity.x_coordinate - star.x_coordinate
        y_delta = entity.y_coordinate - star.y_coordinate
        if (x_delta < 150) and (y_delta < 150):
            path = math.hypot(x_delta, y_delta)

            force = star.weight / path / path

            angle = math.atan2(y_delta, x_delta)

            x_influence = force * math.cos(angle) / 1250
            y_influence = force * math.sin(angle) / 1250
            return -x_influence, -y_influence
        return (0,0)

        pass