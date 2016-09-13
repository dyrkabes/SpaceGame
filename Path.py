import copy

class Path:
    """
    Calculates path points to draw. Simply copies the ship and makes
    the copy to move saving marks on it's way
    """
    def __init__(self, ship):
        self.points = []
        self.ship = copy.copy(ship)
        self.got_to_destination = False

        # when the path is found stops the ship copy
        self.ship.add_path_observer(self.path_found)

    def cycle(self):
        steps = 0

        # problem with infinite loop if the point is unreachable
        global_steps = 0

        while not self.got_to_destination:
            steps += 1
            global_steps += 1
            self.pseudo_act()
            if steps > 6:
                self.points.append((self.ship.x_coordinate, self.ship.y_coordinate))
                steps = 0
            if global_steps > 3333:
                print("Inf loop occured")
                break

    def path_found(self):
        """
        If pseudo ship gets to it's destination it calls path_found() function
        that stops path finding cycle
        :return:
        """
        self.got_to_destination = True

    def pseudo_act(self):
        """
        Calling only movement functions
        :return: None
        """
        self.ship.rotate()
        self.ship.move()



