import Constants


class BilgeManager:
    """
    Class manages filling of the ship's bilges
    """
    @staticmethod
    def select_bilge(ship, target):
        """
        Fills the most empty bilge
        :param ship: ship filling it's bilges
        :param target: object to store
        :return: None. Fills the suitable bilge
        """
        bilges = BilgeManager.get_bilges(ship)
        min_free_space = 10000
        best_bilge = None
        for bilge in bilges:
            if (bilge.space < min_free_space and
                    bilge.space_max - bilge.space >= target.weight):
                min_free_space = bilge.space
                best_bilge = bilge
        if best_bilge:
            best_bilge.fill_bilge(target)

    @staticmethod
    def is_any_bilge_free_enough(ship, target):
        """
        Checks if there're bilges capable to store the target
        :param ship: ship filling it's bilges
        :param target: object to store
        :return: True if there're bilges free enough
        """
        bilges = BilgeManager.get_bilges(ship)
        for bilge in bilges:
            if bilge.space_max - bilge.space >= target.weight:
                return True
        return False

    @staticmethod
    def get_bilges(ship):
        """
        :param ship: ship which bilges we want to get
        :return: all the bilges
        """
        components = ship.get_components()
        bilges = [component for component in components
                  if component.type == Constants.ShipConstants.BILGE]
        return bilges

    @staticmethod
    def analyze_rest_orders(ship):
        """
        Looks for orders that can't be performed
        after filling the bilge
        :param ship: ship that has filled it's bilge
        :return: None. Removes orders impossible to perform
        """
        grabber_orders = [order for order in ship.orders
                          if order.component_type == Constants.ShipConstants.GRABBER]
        for order in grabber_orders:
            if not BilgeManager.is_any_bilge_free_enough(ship, order.target):
                ship.remove_order_by_target(order.target)
