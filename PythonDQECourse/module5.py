# #class and Object

class TestClass:
    def __init__(self ,x):
        self.x = x
    #     self.y = y
    # def myfirstname(self):
    #     print(f'This is my first class, and x = {self.x}')
    #
    # def test_method(self):
    #     self.myfirstname()

# emp = TestClass(100)
# emp2 = TestClass(200)
#
# emp.myfirstname()
# emp2.test_method()
# print(emp.x)
# print(emp2.x)

# #Oop Principles
# #abstraction

class PetClass:
    def __init__(self ,name = 'Muhammad', color = 'Red', sound = 'aaaa'):
        self.name = name
        self.color = color
        self.sound = sound
#
    def make_sound(self):
        print(self.name)
    def make_color(self):
        print(self.sound)
#
# # Test1 = Pet(name = 'test', color = 'color_test')
Test1 = PetClass('ismail')
print(Test1.name)

Test2 = PetClass('blue')
print(Test2.color)

Test2.make_sound()
print(Test2.color)

Test2.make_color()
print(Test2.sound)
