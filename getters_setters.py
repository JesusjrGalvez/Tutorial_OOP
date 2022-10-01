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


jesus = Human("Jesus", 183)
print(jesus.name)
#print(jesus.__name)
#jesus.name = "tom"
print(jesus.name)
jesus.__name = "Jim"
print()
jesus.set_name("James")
print(jesus.name)