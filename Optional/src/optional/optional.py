

class Optional:

    _obj = None

    def __init__(self, obj):
        self._obj = obj

    @classmethod
    def empty(cls):
        return Optional(None)

    @classmethod
    def of(cls, obj):
        return Optional(obj)

    @classmethod
    def OfNoneAble(cls, obj):
        return cls.of(obj) if obj != None else cls.empty()

    def is_present(self):
        return self._obj != None

    def get(self):
        if self.is_present():
            return self._obj
        raise InvalidOperationException(
            "You cannot invoke get() on an empty Optional")

    def if_present(self, consumer):
        if self.is_present():
            return consumer(self._obj)

    def or_else_get(self, consumer):
        return self._obj if self.is_present else consumer()

    def or_else(self, other):
        return self._obj if self.is_present else other

    def or_else_throw(self, exception):
        if self.is_present():
            return self._obj
        raise exception

    def __eq__(self, other):
        if other != None:
            if (not other.is_present()) & (not self.is_present()):
                return True
            if other.is_present() & self.is_present() & other.get().equals(self.get()):
                return True
        return False

    def __hash__(self):
        return self.get().hash() if self.is_present else 0


class InvalidOperationException(Exception):
    pass
