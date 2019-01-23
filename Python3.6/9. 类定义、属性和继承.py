# class Demo:
#
#     def fun1(self):
#         print('1')
#
#     def fun2(self):
#         print('2')
#
#
# a = Demo()
# print(a)
# a.fun1()
# a.fun2()
# a.fun2()


# class Animal:
#     eye = 2
#
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#
#     def play(self):
#         print(self)
#         print('123')
#
#     def demo():
#         print()
#         print('123')
#
#
# a = Animal(name='cat', food='fish')
# # print(a)
# # print(a.eye)
# # print(a.name)
# # print(a.food)
# a.play()
# Animal.demo()
# a.demo()
# # print(Animal.eye)
# # Animal.play('1')

# class Animal(object):  # class Animal
#     eye = 2
#
#     def __init__(self, name, food):
#         print('init')
#         self.name = name
#         self.food = food
#         self.age = 18
#
#     def play(self, number):
#         # print(number+self.age)
#         # print(self.name+self.food)
#         print(number)
#
#     def demo():
#         print('demo')
#
#
# class Cat(Animal):
#     def eat(self):
#         print('eat')
#
#     def play(self):
#         print('cat play')
#
#
# small_cat = Cat(name='small cat', food='small fish')
# print(small_cat.food)
# small_cat.play()
# small_cat.eat()

# class Student(object):
#     """
#     return student information
#     """
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def get_name(self):
#         if isinstance(self.name, str):
#             return self.name
#
#     def get_age(self):
#         if isinstance(self.age, int):
#             return self.score
#
#     def get_score(self):
#         if isinstance(self.score, int):
#             return self.score
#
#
# zyx = Student('zhengyx', 24, 60)
# print(zyx.get_name())
# print(zyx.get_age())
# print(zyx.get_score())


# class ClassName(object):
#     def fun1(self):
#         print('this is fun1')
#
#     def fun2(self):
#         print('this is fun2')
#
#
# cla = ClassName()
# cla.fun1()
# cla.fun2()

# class Animal(object):
#     eye = 2
#
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#
#     def play(self):
#         print('haha')
#
#
# minions = Animal('minions', 'banana')
# minions.play()
# dog = Animal('dog', 'bone')
# dog.play()
# print(Animal.eye)
# print(dog.eye)
# print(Animal.name)


# class A:
#     def play(self):
#         print('haha')
#
#
# class B(A):
#     pass
#
#
# b = B()
# b.play()


# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# r = Rectangle(10, 20)
# print(r.area())
#
#
# class Square(Rectangle):
#     def is_square(self):
#         return self.length == self.width
#
#
# s = Square(10, 10)
# print(s.is_square())


# class Root:
#     __total = 0
#
#     def __init__(self, v):
#         self.__value = v
#         Root.__total += 1
#
#     def show(self):
#         print('self.__value: ', self.__value)
#         print('Root.__total: ', Root.__total)
#
#     @classmethod
#     def class_show_total(cls):
#         print(cls.__total)
#
#     @staticmethod
#     def static_show_total():
#         print(Root.__total)
#
#
# r = Root(3)
# r.class_show_total()
# r.static_show_total()
# r.show()
# Root.class_show_total()
# Root.static_show_total()
# Root.show(r)
# r.show()
# rr = Root(5)
# r.show()
# Root.show(rr)
# rr.show()
# print('*' * 8)
# r.show()
# Root.show(r)
# r.class_show_total()
# Root.class_show_total()
# r.static_show_total()
# Root.static_show_total()


# class Test(object):
#     def __init__(self, value):
#         self.__value = value
#
#     def __get(self):
#         return self.__value
#
#     def __set(self, v):
#         self.__value = v
#
#     def __del(self):
#         del self.__value
#
#     value = property(__get, __set, __del)
#
#     def show(self):
#         print(self.__value)
#
#
# t = Test(3)
# t.show()
# print(t.value)
# t.value = 5
# t.show()
# print(t.value)
# del t.value
# t.value = 1
# t.show()
# print(t.value)

# homework for last class
class Rectangle(object):
    # def __init__(self, length, width):
    #     self.length = length
    #     self.width = width
    #     self.area()

    def area(self):
        print(self.length * self.width)
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area()
        self.judgment()

    def judgment(self):
        if self.length == self.width:
            print(1)
        else:
            print(0)


a = Square(3, 3)

# a1 = Rectangle(2, 3)
# print(a1.area())
