class Human:
    def __init__(self, name: str, height: float):
        self.__name = name
        self.height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, new_name):
        self.__name = new_name
        return self.__name

# https://stackoverflow.com/questions/4555932/public-or-private-attribute-in-python-what-is-the-best-way
class Foo():
    def __init__(self):
        self.__attr = 0

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        self.__attr = value

    @attr.deleter
    def attr(self):
        del self.__attr




f = Foo()
print(f.attr)
print(f.__dict__)
f.__attr = 1
print(f.attr)
print(f.__dict__)
#print(f.__attr)

'__attr' in f.__dir__()

#f.__getattribute__('__attr')


jesus = Human("Jesus", 185)
print(jesus.name)
print(jesus.__dict__)
jesus.__name = "Tom"
print(jesus.__name)