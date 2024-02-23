#1.1
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off.")

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"{self.brand} {self.model} is making {self.coffee_type} coffee.")

class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.brand} {self.model} is blending at speed level {self.speed_levels}.")

class MeatGrinder(Device):
    def __init__(self, brand, model, grind_type):
        super().__init__(brand, model)
        self.grind_type = grind_type

    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat for {self.grind_type}.")

coffee_machine = CoffeeMachine("BrandX", "CM123", "Espresso")
coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender = Blender("BrandY", "BL456", 3)
blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("BrandZ", "MG789", "sausages")
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()
#1.2
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def sail(self):
        print(f"The ship {self.name} is sailing.")

    def anchor(self):
        print(f"The ship {self.name} is anchoring.")

class Frigate(Ship):
    def __init__(self, name, size, missile_type):
        super().__init__(name, size)
        self.missile_type = missile_type

    def fire_missile(self):
        print(f"The frigate {self.name} is firing {self.missile_type} missile.")

class Destroyer(Ship):
    def __init__(self, name, size, weapon_type):
        super().__init__(name, size)
        self.weapon_type = weapon_type

    def attack_target(self):
        print(f"The destroyer {self.name} is attacking the target with {self.weapon_type}.")

class Cruiser(Ship):
    def __init__(self, name, size, num_cannons):
        super().__init__(name, size)
        self.num_cannons = num_cannons

    def fire_cannons(self):
        print(f"The cruiser {self.name} is firing {self.num_cannons} cannons.")

frigate_ship = Frigate("FrigX", "Medium", "Guided")
frigate_ship.sail()
frigate_ship.fire_missile()
frigate_ship.anchor()

destroyer_ship = Destroyer("DestroyY", "Large", "Torpedo")
destroyer_ship.sail()
destroyer_ship.attack_target()
destroyer_ship.anchor()

cruiser_ship = Cruiser("CruisZ", "Huge", 10)
cruiser_ship.sail()
cruiser_ship.fire_cannons()
cruiser_ship.anchor()



#2.1
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class CircleInSquare(Square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def radius(self):
        return self.side_length / 2

    def area(self):
        return 3.14 * self.radius()**2 


square_obj = Square(4)
print(f"Площадь квадрата: {square_obj.area()}")

circle_in_square_obj = CircleInSquare(4)
print(f"Радиус вписанной окружности: {circle_in_square_obj.radius()}")
print(f"Площадь вписанной окружности: {circle_in_square_obj.area()}")


#2.2

class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)


car_obj = Car(number_of_wheels=4, horsepower=200, number_of_doors=4)
print(f"Количество колес: {car_obj.number_of_wheels}")
print(f"Мощность двигателя: {car_obj.horsepower} л.с.")
print(f"Количество дверей: {car_obj.number_of_doors}")
#2.3
import pickle

class Shape:
    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square: Top-left corner ({self.x}, {self.y}), Side length: {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle: Top-left corner ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Circle: Center ({self.x}, {self.y}), Radius: {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Ellipse: Top-left corner ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")

shapes = [Square(0, 0, 5), Rectangle(2, 2, 6, 4), Circle(1, 1, 3), Ellipse(3, 3, 5, 2)]
for shape in shapes:
    shape.show()
    shape.save("shapes.pkl")

loaded_shapes = [Shape.load("shapes.pkl") for _ in range(len(shapes))]
for loaded_shape in loaded_shapes:
    loaded_shape.show()
