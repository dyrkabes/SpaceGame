import Constants
import TextConstants

from managers.BilgeManager import BilgeManager
from Order import Order

from view.AimMarker import AimMarker

class OrderHelper:
    """
    Handles creation of new orders for a ship
    """
    @staticmethod
    def is_order(ship, target):
        # if order was the same as an already created one
        if hasattr(target, "component_type"):
            for order in ship.orders:
                if target == order.target:
                    if order.component_type == Constants.ShipConstants.WEAPON:
                        for aim_marker in ship.aim_markers:
                                if aim_marker.target.component_type == Constants.ShipConstants.WEAPON:
                                    ship.aim_markers.remove(aim_marker)
                                    aim_marker.destroy()
                    ship.orders.remove(order)
                    # just cancelling the order, not creating new one
                    return True
                    break
        return False

    @staticmethod
    def process_order(ship, target):
        #
        if target.component_type == Constants.ShipConstants.GRABBER:
                OrderHelper.grabber_order_process(ship, target)

        elif target.component_type == Constants.ShipConstants.WEAPON:
            # checking if the ship already had a weapon related order
            OrderHelper.weapon_order_process(ship, target)

    @staticmethod
    def grabber_order_process(ship, target):
        """
        Processes new grabber order. Either creates a new order
        or creates an info label with the reason
        why order's creation is impossible
        """
        if target.weight <= ship.get_component(target.component_type).power:
            if BilgeManager.is_any_bilge_free_enough(ship, target):
                ship.orders.append(Order(target, ship.remove_order_by_target))
            else:
                ship.state_manager.new_message(TextConstants.Messages.BILDGE_NOT_ENOUGH_SPACE, urgent=True)
        else:
            ship.state_manager.new_message(TextConstants.Messages.GRABBER_NOT_ENOUGH_POWER, urgent=True)

    @staticmethod
    def weapon_order_process(ship, target):
        for order in ship.orders:
            if order.component_type == Constants.ShipConstants.WEAPON:
                # removing the old ones
                for aim_marker in ship.aim_markers:
                        if aim_marker.target.component_type == Constants.ShipConstants.WEAPON:
                            ship.aim_markers.remove(aim_marker)
                            aim_marker.destroy()
                ship.orders.remove(order)
                # TODO: when there will be more than one weapon add weapon ID

        # creating new order for the ship's component
        ship.orders.append(Order(target, ship.remove_order_by_target))
        # if it is the player's ship creating an aim marker
        if ship.player_ship:
            OrderHelper.create_aim_marker(ship, target)

    @staticmethod
    def create_aim_marker(ship, target):
        # Creates aim marker
        aim_marker = AimMarker(target)
        ship.object_processor_create_entity(
            aim_marker
        )
        target.register_destroy_observer(aim_marker)
        ship.aim_markers.append(aim_marker)
