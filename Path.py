import copy

class Path:
    def __init__(self, ship):
        self.points = []
        self.ship = copy.copy(ship)
        self.ship.add_path_observer(self.path_found)
        # inits the last point
        # probably we will just copy 100% of the ship and make it run in our pseudocycle. And we could use the old ship and return it after but it's trashy
        # get the end point
        # get speeds - angle and movement
        pass

    def cycle(self):
        self.got_to_destination = False
        steps = 0

        #zaplatka
        global_steps = 0

        while not self.got_to_destination:
            steps += 1
            global_steps += 1
            self.pseudo_act()
            # self.ship.act()
            if steps > 6:
                self.points.append((self.ship.x_coordinate, self.ship.y_coordinate))
                steps = 0
            # print("This")
            if global_steps > 3333:
                print("WOW")
                break

        # for i in range(7):
        #     self.pseudo_act()
        # self.points.append((self.ship.x_coordinate, self.ship.y_coordinate))


    def path_found(self):
        self.got_to_destination = True

    def pseudo_act(self):
        self.ship.rotate()
        self.ship.move()



