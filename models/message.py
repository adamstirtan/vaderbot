from models.entity import Entity


class Message(Entity):

    def __init__(self, name, message, message_time, entity_id=0):
        Entity.__init__(self, entity_id)
        self._name = name
        self._message = message
        self._message_time = message_time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def message_time(self):
        return self._message_time

    @message_time.setter
    def message_time(self, value):
        self._message_time = value
