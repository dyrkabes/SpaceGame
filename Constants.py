class GeneralConstants:
    SHIP = "ship"
    POINT = "point"
    COMET = "comet"
    STAR = "star"
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



