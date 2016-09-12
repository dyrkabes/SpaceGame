import Constants

class BilgeManager:
    @staticmethod
    def select_bilge(ship, target):
        bilges = BilgeManager.get_bilges(ship)

        min = 1000
        best_bilge = None
        for bilge in bilges:
            if (bilge.space < min) and (bilge.space_max - bilge.space >= target.weight):
                min = bilge.space
                best_bilge = bilge
        if best_bilge:
            best_bilge.fill_bilge(target)

    @staticmethod
    def is_any_bilges_free_enough(ship, target):
        bilges = BilgeManager.get_bilges(ship)
        for bilge in bilges:
            if bilge.space_max - bilge.space >= target.weight:
                print(bilge.space_max-bilge.space)
                return True
        return False

    @staticmethod
    def get_bilges(ship):
        components = ship.get_components()
        bilges = [component for component in components if component.type == Constants.ShipConstants.BILGE]
        return bilges

    @staticmethod
    def analyze_rest_orders(ship):
        grabber_orders = [order for order in ship.orders if order.component_type == Constants.ShipConstants.GRABBER]
        for order in grabber_orders:
            if not BilgeManager.is_any_bilges_free_enough(ship, order.target):
                ship.remove_order_by_target(order.target)


