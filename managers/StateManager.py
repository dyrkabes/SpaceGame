from managers.MessageManager import MessageManager

class StateManager:
    def __init__(self):
        self.message_manager = MessageManager()
        self.messages = []
        # For on pause messages
        self.urgents = False

    def new_message(self, message, urgent=False):
        self.messages.append((message, urgent))
        if urgent:
            self.urgents = True

    def pop_message(self, urgent=False):
        if not urgent:
            return self.messages.pop()[0]
        else:
            # messages that occur during pause
            urgent_messages = [message for message in self.messages if message[1]]
            if len(urgent_messages) == 1:
                self.urgents = False
            message = urgent_messages.pop()
            self.messages.remove(message)
            return message[0]


