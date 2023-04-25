from time import time

class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v = Vector()
v.x = 5
v1 = Vector()
v1.x = 200
print(v.x)