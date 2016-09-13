import Constants


class OrderAnalyzer:
    """
    Class manages weapon orders of AI ships.
    In the feature it will also give grabber orders
    and obviously they won't be so hard coded :)
    """
    @staticmethod
    def select_target(ship, current_system):
        """
        Selects a target for the ship
        """
        if not ship.player_ship:
            if not ship.orders:
                entity = [entity for entity in current_system.entities
                          if (entity.type == Constants.GeneralConstants.SHIP and
                              entity.player_ship)]
                if entity:
                    entity = entity.pop()
                    ship.create_order(entity)
