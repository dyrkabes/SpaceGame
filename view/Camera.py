import Settings
import CurrentSystem

class Camera:
    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 0

    def init_current_system_parameters(self, current_system):
        self.current_system = current_system


    def move(self, x_coordinate, y_coordinate):
        self.x_coordinate += x_coordinate
        self.y_coordinate += y_coordinate

    def move_to(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate



        #TODO : Check if object can hang from the edge of the map
        # if self.x_coordinate + Settings.screen_width / Settings.GRID_SIZE >  self.current_system.world_size:
        #     self.x_coordinate = ( self.current_system.world_size - Settings.screen_width / Settings.GRID_SIZE)
        # elif self.x_coordinate < 0:
        #     self.x_coordinate = 0
        #
        # if self.y_coordinate + Settings.screen_height / Settings.GRID_SIZE >  self.current_system.world_size:
        #     self.y_coordinate =  self.current_system.world_size - (Settings.screen_height / Settings.GRID_SIZE)
        # elif self.y_coordinate < 0:
        #     self.y_coordinate = 0

            #max min ?