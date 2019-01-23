# a  # NameError: name 'a' is not defined

# int('test')  # ValueError: invalid literal for int() with base 10: 'test'

# li = []
# print(li[2])  # IndexError: list index out of range

# d = {}
# print(d['1'])  # KeyError: '1'

# import numbas  # ModuleNotFoundError: No module named 'numbas'

# import numpy
# numpy.aso  # AttributeError: module 'numpy' has no attribute 'aso'

# for i in range(100)  # SyntaxError: invalid syntax


# def demo():
#     try:
#         # a = 1   # 代码块
#         # a
#         f = open('1', 'r')
#     except NameError as e:  # 捕获异常
#         #  except FileNotFoundError as e:
#         print(e, 'NameError')
#         return e
#     except FileNotFoundError as e:
#         print(e, 'FileNotFoundError')
#         raise e
#         # return e
#     except Exception as e:
#         print(e, 'Exception')
#         return e
#     else:
#         print('else')
#     finally:
#         print('finally')
#
#
# # print(demo())
# print(demo())
# print('123')


# with open('1', 'w'):
#     print(123)
#
# f = open('2', 'w')
# f.close()

# demo()

# s = input('>:')
# if not isinstance(s, str):
#     raise TypeError('{} is wrong type, str expected'.format(s))


# def fun():
#     print(1/0)
#
#
# def sdemo():
#     try:
#         fun()
#     except Exception:
#         raise
#
#
# sdemo()


# try:
#     a = int(input('a-->:'))
#     b = int(input('b-->:'))
#     print(a / b)
# except Exception as e:
#     print(e)
# else:
#     print('else')

# assert 1 == 4, 'wrong length'

# for i in Exception.__subclasses__():
#     print(i)


# def file_test():
#     try:
#         a = ['a', 'b', 'c']
#         file = open('test.txt', 'r')
#         file.readlines()
#     except FileNotFoundError as e:
#         return e
#     except Exception as e:
#         raise Exception(e)
#     else:
#         print('open OK!')
#         file.close()
#     finally:
#         # print(a)
#         del a
#
#
# print(file_test())

# assert 1 == 1, '1 == 1'
# assert 1 == 2, '1 == 2'

# *_coding=UTF-8_*_
# 使用自定义异常类实现指定输入字符串长度
# 自定义异常类
# class SomeCustomError(Exception):
#     def __init__(self, str_length):
#         super(SomeCustomError, self).__init__()
#         self.str_length = str_length
#
#
# # 使用自定义异常
# length = int(input("输入指定输入字符串长度范围:\n"))
# while True:
#     try:
#         s = input("输入一行字符串:\n")
#         # 输入字符串长度超过指定长度范围,引发异常
#         if length < len(s):
#             raise SomeCustomError(length)
#     except SomeCustomError as x:
#         print('捕获自定义异常')
#         print('输入字符串重读应该小于%d,请重新输入!' % x.str_length)
#     else:
#         print('输入字符串为%s' % s)
#         break
#

# # print("\033[1;31;40m您输入的帐号或密码错误！\033[0m")
# print('\033[0;30;47mThis is what I want to print.\033[0m')
# exit()

# print('\n'.join(dir(Exception)))
# exit()


# class ShortInputException(Exception):
#     def __init__(self, str_length):
#         self.str_length = str_length
#
#
# length = int(input('input the maximum length of string: \n'))
# while True:
#     try:
#         s = input('input a string: \n')
#         if length < len(s):
#             raise ShortInputException(length)
#     except ShortInputException as e:
#         print('ShortInputException: input string should be shorter than {} letters.'
#               .format(length))
#     else:
#         print('input string is {}'.format(s))
#         break


# be = BaseException('BaseException')
# print(str(be))

#
# import sys
#
#
# try:
#     a
# except NameError:
#     tb = sys.exc_info()[2]
#     print(type(tb))
#     raise NameError().with_traceback(tb)

# li = []
# li[2]


# d = {2: 1}
# d[2]


# class ShortInputException(Exception):
#     """
#     customize exception class
#     """
#     def __init__(self, length, at_least):
#         Exception.__init__(self)
#         self.length = length
#         self.at_least = at_least
#
#
# try:
#     s = input('please input-->')
#     if len(s) < 3:
#         raise ShortInputException(len(s), 3)
# except EOFError:
#     print('you have input an EOF mark')
# except ShortInputException as x:
#     print('ShortInputException: you have input {} letters, the minimum length is {}!'
#           .format(x.length, x.at_least))
# else:
#     print('no exception occurs')


# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     # def __str__(self):
#     #     return repr(self.value)
#
#
# try:
#     raise MyError(2 * 2)
# except MyError as e:
#     print('my exception occurred, value:', e.value)
#
# raise MyError('oops')


# class Error(Exception):
#     pass
#
#
# class InputError(Error):
#     """
#     Exception raised for errors in the input.
#     Attributes:
#         expression --input expression in which the error occurred
#         message --explanation of the error
#     """
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message
#
#
# class TransitionError(Error):
#     """
#     Raised when an operation attempts a state transition that's not allowed.
#     Attributes:
#         previous --state at beginning of transition
#         next --attempted new state
#         message --explanation of why the specific transition is not allowed
#     """
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message
#


# while True:
#     try:
#         a = int(input('please enter a number: '))
#         break
#     except ValueError:
#         print('That was not a valid number. Try again...')

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#     x, y = inst.args
#     print('x =', x)
#     print('y =', y)


# a_list = ['China', 'America', 'England', 'France']
# print('Please input the index of string')
# while True:
#     n = int(input())
#     try:
#         print(a_list[n])
#     except IndexError:
#         print('list index out of range or wrong index, please re-input')
#     else:
#         break


# try:
#     x = input('please input dividend: ')
#     y = input('please input divisor: ')
#     z = float(x) / float(y)
# except ZeroDivisionError:
#     print('divisor can not be zero')
# except ValueError:
#     print('dividend and divisor should be numbers')
# except NameError:
#     print('variable was not defined')
# else:
#     print(x, '/', y, '=', z)


# import sys
# try:
#     f = open('1.txt')
#     s = f.readline()
#     i = int(s.strip())
# except (OSError, ValueError, RuntimeError, NameError):
#     print('error occurred')


# f = open('123.txt')
# s = f.readline()
# i = int(s.strip())


# try:
#     3 / 0
# except ZeroDivisionError:
#     print(3)
# finally:
#     print(5)


# try:
#     f = open('1.txt', 'r')
#     line = f.readline()
#     print(line)
# finally:
#     f.close()


# try:
#     f = open('test.txt', 'r')
#     line = f.readline()
#     print(line)
# finally:
#     f.close()

# try:
#     3 / 0
# finally:
#     print(5)


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print('division by zero!')
#     else:
#         print('result is:', result)
#     finally:
#         print('executing finally clause')
#
#
# divide('2', '1')

# def demo_div(a, b):
#     try:
#         return a / b
#     # except:
#     #     pass
#     # finally:
#     #     return -1
#
#
# print(demo_div(10, 2))

# try:
#     assert 1 == 2, '1 is not equal 2!'
# except AssertionError as e:
#     print('\033[0;31m{}: \033[0m{}'.format(e.__class__.__name__, e))
#     pass

# with open('1.txt', 'r') as fr:
#     line = fr.readlines()
#     print(line)

# import sys
# try:
#     1 / 0
# except:
#     t = sys.exc_info()
#     print(t)


# import sys
#
#
# def a():
#     1 / 0
#
#
# def b():
#     a()
#
#
# def c():
#     b()
#
#
# try:
#     c()
# except:
#     r = sys.exc_info()
#     print(r)


# with open('data.txt', 'r') as fp:
#     data = fp.readlines()
# data = [int(line.strip()) for line in data]
# data.sort()
# # data = [str(i) + '\n' for i in data]
# data = '\n'.join([str(i) for i in data])
# with open('data_asc.txt', 'w') as fp:
#     fp.writelines(data)


# import pdb
#
#
# n = 37
# pdb.set_trace()
# for i in range(2, n):
#     if n % i == 0:
#         print('Np')
#         break
#     else:
#         print('Yes')


# class MyError(Exception):
#     def __init__(self, msg):
#         # self.msg = msg
#         super().__init__(msg)
#
#
# try:
#     raise MyError('customized error')
# except MyError as e:
#     print(e)
#     print('my msg:', e)
#     # raise e
