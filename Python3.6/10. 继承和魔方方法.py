# class Animal:
#     def eat(self):
#         print('eat', self.name)
#
#     def drink(self):
#         print('drink', self.name)
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('eat2')
#
#
# c1 = Cat('1')
# c1.eat()
# c1.drink()


# class Base(object):
#     def play(self):
#         print('Base')
#
#
# class A(Base):
#     def play(self):
#         print('A')
#
#
# class B(Base):
#     def play(self):
#         print('B')
#
#
# class C(A, B):
#     def play(self):
#         super(A, self).play()
#         pass
#
#
# c = C()
# c.play()
# print(C.mro())

# class A(object):
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#
# class B(object):
#     def __init__(self, age):
#         self.age = age
#
#     def __add__(self, other):
#         print('add')
#
#     def __radd__(self, other):
#         print('radd')
#
#     def __str__(self):
#         print('__str__')
#         return str(self.age)
#
#
# a = A(18, 'abc')
# b = B(12)
# a + b
# print(b)


# class Base:
#     def play(self):
#         # super().play()
#         print('this is Base')
#
#
# class A(Base):
#     def play(self):
#         super().play()
#         print('this is A')
#
#
# class B(Base):
#     def play(self):
#         super().play()
#         print('this is B')
#
#
# class C(A, B):
#     def play(self):
#         super().play()
#         print('this is C')
#
#     def __add__(self, other):
#         print('__add__')
#
#     def __radd__(self, other):
#         print('__radd__')
#
#     def __str__(self):
#         # print('__str__')
#         return '__str__'
#
#     # def __repr__(self):
#     #     print('__repr__')
#
#     def __call__(self):
#         return 'this is __call__'
#
#
# c = C()
# # c1 = C()
# # b = B()
# # c.play()
# # print(C.mro())
# # c + b
# # b + c
# # print(c)
# # print(c())
# # c.__str__()
# # print(c)
# print(c.__class__)
# # print(c.__base__)
# # print(c.__bases__)
# print(c.__dict__)
# print(c.__doc__)
# print(c.__dir__)

# homework

# class A(object):
#     def __call__(self, *args, **kwargs):
#         return 'this is __call__'
#
#     def __str__(self):
#         return 'this is an instance of class A'
#
#
# a = A()
# print(a())
# print(a)

class A(object):
    def __call__(self, *args, **kwargs):
        print('__call__')

    def __str__(self):
        return '__str__'

    def __repr__(self):
        return '2'


a = A()
a()
print(a)
