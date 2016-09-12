import random

import Constants


class DamageProcessor:
    @staticmethod
    def process_collision(target, damage_inflicter, create_info_label):
        # mojet vybiraem tip vzaimodeistv? tipa ship-ship, comet-ship, ship-star? ne
        collision_type = None

        if ((target.type == Constants.GeneralConstants.SHIP
                and damage_inflicter.type == Constants.GeneralConstants.COMET)
                or
                (target.type == Constants.GeneralConstants.COMET
                and damage_inflicter.type == Constants.GeneralConstants.SHIP)):
            collision_type = Constants.CollisionTypes.SHIP_COMET
        elif ((target.type == Constants.GeneralConstants.STAR
                and damage_inflicter.type == Constants.GeneralConstants.COMET)
                or
                (target.type == Constants.GeneralConstants.COMET
                and damage_inflicter.type == Constants.GeneralConstants.STAR)):
            collision_type = Constants.CollisionTypes.STAR_COMET
        elif ((target.type == Constants.GeneralConstants.BULLET
                and damage_inflicter.type == Constants.GeneralConstants.COMET)
                or
                (target.type == Constants.GeneralConstants.COMET
                and damage_inflicter.type == Constants.GeneralConstants.BULLET)):
            collision_type = Constants.CollisionTypes.BULLET_COMET
        elif ((target.type == Constants.GeneralConstants.BULLET
                and damage_inflicter.type == Constants.GeneralConstants.STAR)
                or
                (target.type == Constants.GeneralConstants.STAR
                and damage_inflicter.type == Constants.GeneralConstants.BULLET)):
            collision_type = Constants.CollisionTypes.BULLET_STAR
        elif ((target.type == Constants.GeneralConstants.BULLET
                and damage_inflicter.type == Constants.GeneralConstants.SHIP)
                or
                (target.type == Constants.GeneralConstants.SHIP
                and damage_inflicter.type == Constants.GeneralConstants.BULLET)):
            collision_type = Constants.CollisionTypes.SHIP_BULLET



        if collision_type == Constants.CollisionTypes.SHIP_COMET or collision_type == Constants.CollisionTypes.SHIP_BULLET:
            # TODO: think about hasattr
            if (hasattr(target, 'ship_id') and hasattr(damage_inflicter, 'ship_id') and target.ship_id != damage_inflicter.ship_id
            or target.type == Constants.GeneralConstants.COMET or damage_inflicter.type == Constants.GeneralConstants.COMET):
                if target.type != Constants.GeneralConstants.SHIP:
                    target, damage_inflicter = damage_inflicter, target
                damage_dealt = DamageProcessor.calc_damage_dealt(target, damage_inflicter)
                create_info_label(target,
                                  str(damage_dealt),
                                  target.state_manager.message_manager.decrease_messages_count)
                DamageProcessor.process_shell_damage(target.get_component(Constants.ShipConstants.SHELL), damage_dealt)
                DamageProcessor.process_component_damage(target)

                damage_inflicter.destroy(target)
                # return damage_inflicter, target

        elif collision_type == Constants.CollisionTypes.STAR_COMET:

            if target.type == Constants.GeneralConstants.COMET:
                target, damage_inflicter = damage_inflicter, target
            damage_inflicter.destroy(target)


        elif collision_type == Constants.CollisionTypes.BULLET_COMET:

            if target.type == Constants.GeneralConstants.COMET:
                target, damage_inflicter = damage_inflicter, target
            damage_inflicter.destroy(target)
            target.destroy(damage_inflicter)
            # damage_inflicter.destroy(damage_inflicter)

        elif collision_type == Constants.CollisionTypes.BULLET_STAR:
            if target.type == Constants.GeneralConstants.BULLET:
                target, damage_inflicter = damage_inflicter, target
            damage_inflicter.destroy(target)



            #TODO: FALLS







        # if target.type == Constants.GeneralConstants.SHIP:
        #     damage_dealt = DamageProcessor.calc_damage_dealt(target, damage_inflicter)
        #     DamageProcessor.process_shell_damage(target.get_component(Constants.ShipConstants.SHELL), damage_dealt)
        #     DamageProcessor.process_component_damage(target)



    @staticmethod
    def process_damage(target, damage_inflicter):
        damage_dealt = DamageProcessor.calc_damage_dealt(target, damage_inflicter)
        DamageProcessor.process_shell_damage(target.get_component(Constants.ShipConstants.SHELL), damage_dealt)
        DamageProcessor.process_component_damage(target)



        # if target.type == Constants.GeneralConstants.SHIP:
        #     damage_dealt = DamageProcessor.calc_damage_dealt(damage_inflicter, target)
        #     DamageProcessor.process_shell_damage(target.get_component(Constants.ShipConstants.SHELL), damage_dealt)
        #     DamageProcessor.process_component_damage(target)

    #TODO : calc damage dealt in another way obv
    @staticmethod
    def calc_damage_dealt(target, damage_inflicter):
        return damage_inflicter.damage_dealt()

    @staticmethod
    def process_shell_damage(shell, damage):
        shell.decrease_hitpoints(damage)

    @staticmethod
    def process_component_damage(target):
        dice = random.randint(0, 100)
        if dice > 5:
            components = target.get_components()
            component = random.choice(components)
            component.get_damage(1)
            #test part
            # engine = target.get_component(Constants.ShipConstants.ENGINE)
            # engine.get_damage(5)




        pass