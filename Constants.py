class GeneralConstants:
    SHIP = "ship"
    POINT = "point"
    COMET = "comet"
    STAR = "star"
    PLANET = "planet"
    PLANET_SHADE = "planet_shade"
    OUTER_SPACE_OBJECT = "outer_space_object"
    BULLET = "bullet"
    TEXT = "text"
    AIM_MARKER = "aim_marker"
    EXPLOSION = "explosion"

class ShipConstants:
    ENGINE = "engine"
    SHELL = "shell"
    GRABBER = "grabber"
    BILGE = "bilge"
    WEAPON = "weapon"
    MOVING = "moving"

    SHOT_DELAY = 6
    SHOTGUN_SPREAD = 5

class GUIConstants:
    PRESSED = "pressed"
    DEFAULT = "default"
    BUTTON = "button"
    INVENTORY = "inventory"
    INFO_PLATE = "info_plate"
    CLICK = "click"
    HOVER = "hover"

class StateConstants:
    RUNNING = "running"
    WAITING = "waiting"
    OUTER_SPACE = "outer_space"
    PIT_STOP = "pit_stop"
    LANDED = "landed"
    LANDING = "landing"

class CollidableTypes:
    BULLET = "bullet"
    COLLIDABLE = "collidable"
    COLLIDE_TARGET = "collide_target"
    NON_COLLIDABLE = "non_collidable"

class CollisionTypes:
    SHIP_COMET = "ship_comet"
    STAR_COMET = "star_comet"
    BULLET_COMET = "bullet_comet"
    BULLET_STAR = "bullet_star"
    SHIP_BULLET = "ship_bullet"

class ModuleTypes:
    BULLET_SPEED = "bullet_speed"
    BULLET_DAMAGE = "bullet_damage"
    BULLET_DURATION = "bullet_duration"
    BULLET_CORRUPTION = "bullet_corruption"

    WEAPON_AIM_REANGE = "aim_range"
    WEAPON_RELOAD = "reload"

    AMOUNT_OF_SHOTS = "amount_of_shots"
    SHOTGUN = "shotgun"

    ENGINE_SPEED = "movement_speed"
    ENGINE_ROTATION_SPEED = "rotation_speed"

class ZDimensions:
    # types and z dimensions I meant
    types_and_zs = [
    (GeneralConstants.SHIP, 10),
    (GeneralConstants.POINT, 9),
    (GeneralConstants.COMET, 10),
    (GeneralConstants.STAR, 0),
    (GeneralConstants.PLANET, 0),
    (GeneralConstants.PLANET_SHADE, 1),
    (GeneralConstants.OUTER_SPACE_OBJECT, 9),
    (GeneralConstants.BULLET, 10),
    (GeneralConstants.TEXT, 11),
    (GeneralConstants.AIM_MARKER, 11),
    (GeneralConstants.EXPLOSION, 11)
    ]

    @staticmethod
    def get_z(type):
        for item in ZDimensions.types_and_zs:
            if item[0] == type:
                return item[1]

class ZoomsInLandedState:
    # Probably not the best way. Tho:
    # Pair (type, default_grid_size)
    # If None then it chooses current zoom
    types_and_zooms = [
        (GeneralConstants.SHIP, 5),
        (GeneralConstants.POINT, 5),
        (GeneralConstants.COMET, 5),
        (GeneralConstants.STAR, None),
        (GeneralConstants.PLANET, None),
        (GeneralConstants.PLANET_SHADE, None),
        (GeneralConstants.OUTER_SPACE_OBJECT, 5),
        (GeneralConstants.BULLET, 5),
        (GeneralConstants.TEXT, 5),
        (GeneralConstants.AIM_MARKER, 5),
        (GeneralConstants.EXPLOSION, 5)
    ]

    @staticmethod
    def get_zoom_value(type):
        return [item for item in ZoomsInLandedState.types_and_zooms
                if item[0] == type].pop()

