
class Human:
    all = []
    growth = 1.1
    def __init__(self, name: str, height: float, weight: float):
        self.__name = name
        self.height = height
        self.weight = weight
        Human.all.append(self)

    # This encapsulates attributes.
    # Property Decorator. Read-Only Attribute
    @property
    def name(self):
        return self.__name

    # This how to change an encapsulated attribute.
    # @name.setter
    # def set_name(self, new_name):
    #     self.__name = new_name

    # This also works.
    @name.setter
    def name(self, name): # ERROR AttributeError: can't set attribute
        self.__name = name

    def __repr__(self):
        #__repr__ stands for represent
        #return f"Human('{self.name}',{self.height},{self.weight})"  #represent as f-strings
        return f"{self.__class__.__name__}('{self.name}',{self.height},{self.weight})"

    def calculate_bmi(self):
        # You can have a class create an attribute when a method is called.
        self.bmi = 0
        print(f"BMI = {self.weight/(self.height*0.01 * self.height *0.01)}")
    def grow(self):
        self.height = self.height * self.growth

    # Property decorator = Read-only Attribute.
    @property
    def read_only(self):
        return "AAA"

    @classmethod # This is a class method. It works without any instances. You
    # can prompt it without any instances. It is typically used to
    # instanciate objects.

    # classmethods can also be called from an instance. So can static methods.
    def instanciate_people(cls):
        with open("items.csv", 'r') as file:
            csvFile = csv.DictReader(file)
            items = list(csvFile)
        #print(items)
        for item in items:
            #print(item)
            # These are two ways of getting the value of a key in a dictionary.
            Human(
                name = item['name'],
                height = float(item['height']),
                weight = float(item['weight']),
            )
                #name = item.get('name'),
                #height = float(item.get('height')),
                #weight = float(item.get('weight'))
            #)

    @classmethod
    def change_growth(cls, growth):
        cls.growth = growth


    @staticmethod
    def is_integer(n):
        #We will count out the decimals that are .0, ej, 10.0
        if isinstance(n, float):
            return n.is_integer()
        elif isinstance(n, int):
            return True
        else:
            return False


class Child(Human):
    pass


class Car:
    pass
    def __init__(self, year):
        self.year = year

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
jesus = Human("Jesus", 183, 82)
print(Human.all)
maria = Human("Maria", 160, 48)
print(Human.all)
print(f"Human name is {jesus.name}, human height is {jesus.height}")
print(jesus.height)
jesus.calculate_bmi()
jesus.growth=2
jesus.grow()
print(jesus.height)
print(maria.growth)
print(f"Grwoth is {jesus.growth}")
jesus.calculate_bmi()
print(jesus.bmi)
print(type(jesus))
nazaret = Child("Nazaret", 100, 30)
print("--------")
print(Human.all)
print(nazaret)
print(jesus.read_only)

print("--------")
print(jesus.name)

# jesus.read_only = "BBB" # This returns an error





#Human.instanciate_people()
print(f"all human instances{Human.all}")
print(Human.growth)
Human.change_growth(2.5)
print(Human.growth)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
for human in Human.all:
    print(human)

print(Human.is_integer(5.3))

#mycar = Car()
mycar2 = Car(2020)
print(mycar2.year)
mycar2.milage = 6
print(mycar2.milage)


a = set(["Jesus"])
print(a)
b = "Jesus"
def add_to_set(item):
    a = set(["Jesus"])
    if b in a:
      pass
    else:
      a.add(item)
add_to_set(["Maria"])
print(a)

print(Human.is_integer(7.5))
print(Human.is_integer(8.0))
print(Human.is_integer(9))


print("Hola como estas")

print(jesus.name)
#jesus.set_name("javi")
print(jesus.name)
jesus.set_name = "javi"
print(jesus.name)
#jesus.name = "Tommy"
print(jesus.name)
jesus.__name = "Tom"
print(jesus.name)
print(";.......")
print(jesus.__name)
print(jesus.name)
#jesus.set_name("Tommy")
#print(jesus.name)


