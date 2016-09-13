class MessageManager:
    """
    Calculates offsets for messages.
    Needs some rework soon (slots for messages)
    """
    def __init__(self):
        self.messages_count = 0
        self.messages_offset_y = 0
        self.offset_default = 4
        pass

    def add_message(self):
        self.messages_count += 1
        self.messages_offset_y = self.offset_default * self.messages_count

    def get_offset_x(self):
        return 0

    def get_offset_y(self):
        return self.messages_offset_y

    def decrease_messages_count(self):
        self.messages_count -= 1
        self.messages_offset_y = self.offset_default * self.messages_count

