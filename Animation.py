class Animation:
    def __init__(self, images_names, frame_delay):
        self.images_names = images_names

        self.images_default = []

        self.frame = 0
        self.frame_delay = frame_delay
        self.delay_count = 0

    def animate(self, entity):
        self.delay_count += 1
        if self.delay_count >= self.frame_delay:
            self.process_animation(entity)
            self.delay_count = 0
            entity.zoom_needed = True


    def process_animation(self, entity):
        self.frame += 1
        if self.frame == len(self.images_default):
            self.frame = 0
        entity.image_default = self.images_default[self.frame]