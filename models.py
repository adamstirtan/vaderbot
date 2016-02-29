from abc import ABCMeta, abstractclassmethod


class Entity:

    __metaclass__ = ABCMeta

    def __init__(self, entity_id=0):
        self._entity_id = entity_id

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value

    @abstractclassmethod
    def table_name(self):
        pass

    @abstractclassmethod
    def to_tuple(self):
        pass


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

    def table_name(self):
        return "messages"

    def to_tuple(self):
        return self.name, self.message, self.message_time


class Quote(Entity):

    def __init__(self, quote, points, entity_id=0):
        Entity.__init__(self, entity_id)
        self._quote = quote
        self._points = points

    @property
    def quote(self):
        return self._quote

    @quote.setter
    def quote(self, value):
        self._quote = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    def table_name(self):
        return "quotes"

    def to_tuple(self):
        return self.quote, self.points


class User(Entity):

    def __init__(self, name, entity_id=0):
        Entity.__init__(self, entity_id)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def table_name(self):
        return "users"

    def to_tuple(self):
        return self.name,
