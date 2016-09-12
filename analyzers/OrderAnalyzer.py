import random
import Constants

class OrderAnalyzer:
    @staticmethod
    def select_target(ship, current_system):
        if not ship.player_ship:
            if not ship.orders:

                entities = (entity for entity in current_system.entities)
                entity = [entity for entity in current_system.entities if (entity.type == Constants.GeneralConstants.SHIP and entity.player_ship == True)]
                if entity:
                    entity = entity.pop()
                    ship.create_order(entity)
            #     ship.create_order(random.choice(entities))