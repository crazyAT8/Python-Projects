class BaseClass:
    pass

class Mixin1:
    pass

class Mixin2:
    pass
class SomeClass(BaseClass, Mixin1, Mixin2):
    def __init__(self):
        pass

sc = SomeClass()

print(isinstance(sc, SomeClass))
print(isinstance(sc, BaseClass))
print(isinstance(sc, Mixin1))
print(isinstance(sc, Mixin2))