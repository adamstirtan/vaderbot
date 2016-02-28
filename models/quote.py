from models.entity import Entity


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
