from models.entity import Entity


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
