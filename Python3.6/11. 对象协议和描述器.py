# class Square(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return 'no such attribute'
#
#     # def __getattribute__(self, item):
#     #     print('no such attribute')
#
#
# s = Square('s')
# # print(s)
# s.a = 1
# setattr(s, 'b', 2)
# s.__setattr__('c', 3)
# # print(s.a)
# # s.__getattr__('a')
# # s.__getattr__('d')
# print(s.a)
# print(s.d)


# class A:
#     def __get__(self, instance, owner):
#         print(instance)
#         print(owner)
#         print('__get__')
#
#     def __set__(self, instance, value):
#         print(instance)
#         print(value)
#         print('__set__')
#
#     def __delete__(self, instance):
#         print(instance)
#         print('__delete__')
#
#
# class B:
#     m = A()
#
#     def __del__(self):
#         print('__del__')
#
#
# c = B()
# # print(c.m)
# # c.m = 1
# # del c.m
# delattr(c, 'm')


# # 闭包
# def fun(x):
#     x += 1
#
#     def fun1(y):
#         return x + y
#     return fun1
#
#
# print(fun(1)(2))

# # 闭包传入函数
# def f1(func):
#     print('f1')
#
#     def f2(y):
#         print('f2')
#         return func(y) + 1
#     return f2
#
#
# @f1
# def f3(m):
#     print('f3')
#     return m * m
#
#
# # f3(3) = f1(f3)(3)
# # print(f3(3))
# print(f1(f3))
# # print(f1(f3)(3))


# import time
#
#
# @run_time
# def demo():
#     print('run function demo()')
#
#
# demo()


# class Earth:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self):
#         self.name = 'earth'
#
#
# e = Earth()
# print(e, id(e))
# a = Earth()
# print(a, id(a))

# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
# re = Rectangle(3, 4)
#
# # add
# re.aaa = 1
# setattr(re, 'bbb', 2)
# re.__setattr__('ccc', 3)
# print(dir(re))
#
# # delete
# delattr(re, 'ccc')
# re.__delattr__('bbb')
# # del re
# print(dir(re))
#
# # update
# setattr(re, 'length', 6)
# print(re.length)
# re.__setattr__('length', 5)
# print(re.length)
#
# # find
# print(hasattr(re, 'length'))
# # True
# print(getattr(re, 'length'))
# # 5
# print(re.__getattribute__('length'))
# # 5


# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def __getattr__(self, item):
#         print('no attribute')
#         return 'error'
#
#
# re = Rectangle(3, 4)
# print(getattr(re, 'length'))
# print(re.__getattribute__('length'))
# # 3
# getattr(re, 'aaa')
# # no attribute
# print(re.aaa)
# # no attribute
# # error


# class MyAttribute(object):
#     def __get__(self, instance, owner):
#         print('get')
#
#     def __set__(self, instance, value):
#         print('set')
#
#     def __delete__(self, instance):
#         print('delete')
#
#
# class MyClass(object):
#     m = MyAttribute()
#
#     def __del__(self):
#         print('del')
#
#
# c = MyClass()
# c.m
# # get
# c.m = 1
# # set
# del c.m
# # delete
# # del


# def f1(func):
#     def f2(y):
#         print('f2 running')
#         return func(y) + 1
#     return f2
#
#
# def gun(m):
#     print('gun running')
#     return m * m
#
#
# @f1
# def demo(m):
#     print('this is demo')
#     return m * m
#
#
# print(gun(3))
# # 9
# print(demo(3))
# # f2 running
# # this is demo
# # 10


# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         areas = self.length * self.width
#         return areas
#
#     @property
#     def area(self):
#         return self.length * self.width
#
#     @staticmethod
#     def func():
#         print('static method')
#
#     @classmethod
#     def show(cls):
#         print(cls)
#         print('show fun')
#
#
# re = Rectangle(3, 4)
# print(re.area)
# # 12
# re.func()
# # static method
# re.show()
# # <class '__main__.Rectangle'>
# # show fun


# class TestClass(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('class')
#         return self.func
#
#
# @TestClass
# def fun_test():
#         print('this is test function')
#
#
# print(fun_test())
# # class
# # <function fun_test at 0x000002F075233E18>


# view run time
# import time
#
#
# def run_time(func):
#     def new_fun(*args, **kwargs):
#         t0 = time.time()
#         print('start time: %s' % (time.strftime('%x', time.localtime())))
#         back = func(*args, **kwargs)
#         for i in range(100000):
#             back = func(*args, **kwargs)
#         print('end time:%s' % (time.strftime('%x', time.localtime())))
#         print('run time:%s' % (time.time() - t0))
#         return back
#     return new_fun
#
#
# a = [1, 2, 3]
# print("'use function type'")
# run_time(type)(a)
# print("'use function isinstance'")
# run_time(isinstance)(a, list)


# class A:
#     pass
#
#
# s = A()
# s.a = 1
# print(getattr(s, 'a'))


# import time
#
#
# def run_time(func):
#     def new_fun(*args, **kwargs):
#         t0 = time.time()
#         print('start time: %s' % (time.strftime('%x', time.localtime())))
#         back = func(*args, **kwargs)
#         print('end time:%s' % (time.strftime('%x', time.localtime())))
#         print('run time:%f' % (time.time() - t0))
#         return back
#     return new_fun
#
#
# @run_time
# def test_type():
#     for _ in range(10000):
#         type(1) == 'int'
#
#
# @run_time
# def test_isinstance():
#     for _ in range(10000):
#         isinstance(1, int)
#
#
# test_type()
# print('*' * 8)
# test_isinstance()


def a(func):
    print('a')
    return func


def b(func):
    print('b')
    return func


def c(func):
    print('c')
    return func


def d(func):
    print('d')
    return func


@a
@b
@c
@d
def f():
    print('f')


f()
