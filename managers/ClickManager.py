import Constants
import Settings

class ClickManager:
    " Processes clicks outside GUI"
    
    @staticmethod
    def instance_clicked(mouse_pos, current_system):
        x_mouse_pos = mouse_pos[0]
        y_mouse_pos = mouse_pos[1]
        for entity in current_system.get_entities():
             if entity.x_coordinate - entity.x_size / 2 < x_mouse_pos < entity.x_coordinate + entity.x_size / 2:
                if entity.y_coordinate - entity.y_size / 2 < y_mouse_pos  < entity.y_coordinate + entity.y_size / 2:
                    return entity
        return None
            
        