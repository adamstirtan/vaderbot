class Entity:

    def __init__(self, entity_id=0):
        self._entity_id = entity_id

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
