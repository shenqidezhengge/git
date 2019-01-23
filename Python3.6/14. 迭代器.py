# import time
#
# start = time.time()
# for _ in range(10000):
#     li = []
#     for i in range(11):
#         li.append(i)
# # print(li)
# end = time.time()
# print(end - start)
#
# start = time.time()
# for _ in range(10000):
#     li = list(range(11))
# # print(li)
# end = time.time()
# print(end - start)
#
# start = time.time()
# for _ in range(10000):
#     li = [i for i in range(11)]
# # print(li)
# end = time.time()
# print(end - start)


# li = [i for i in range(11) if i % 2 == 0]
# print(li)
# li = [i if i % 2 == 0 else 0 for i in range(11)]
# print(li)
# li = [i if i % 2 == 0 for i in range(11)]

# se = {i for i in range(11)}
# print(se)
# print(type(se))
#
# li = [i for i in range(11)]
# di = {i: j for i, j in enumerate(li)}
# print(di)
# print(type(di))


# tu = (i for i in range(11))
# print(type(tu))
# print(tu)
# print(tuple(tu))


# li = [i for i in range(11)]
# it = iter(li)
# print(type(it))
# print(next(it))
# print('\n'.join(dir(iter)))

# li = [i for i in range(11)]
# it = iter(li)
# print(next(it))
# print(it.__next__())
# try:
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print('no more value')


# class IterDemo(object):
#     def __init__(self, lis):
#         self.lis = lis
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index < len(self.lis):
#             number = self.lis[self._index]
#             self._index += 1
#             return number
#         else:
#             raise StopIteration
#
#
# li = [1, 2, 3, 4, 5]
# s = IterDemo(li)
# print(s)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))


# def fun(end):
#     n, a, b = 0, 0, 1
#     while n < end:
#         print('+' * 8, b)
#         yield b
#         print('-' * 8, b)
#         a, b = b, a + b
#         n += 1
#
#
# s = fun(10)
# print(list(s))

def func(end):
    n, a, b = 0, 0, 1
    while n < end:
        print('*' * 8, b)
        yield b
        print('*' * 8, b)
        n += 1


s = func(10)
print(next(s))
