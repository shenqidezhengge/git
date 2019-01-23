# def dict_tuple_exchange(d, t):
#     d1 = d.copy()
#     t1 = tuple(d.values())
#     i = 0
#     for keys in d.keys():
#         d1.update({keys: t[i]})
#         i += 1
#     return d1, t1
#
#
# di = {'a': 1, 'b': 2, 'c': 3}
# tu = (4, 5, 6)
# di1, tu1 = dict_tuple_exchange(di, tu)
# print('before exchange')
# print(di)
# print(tu)
# print('after exchange')
# print(di1)
# print(tu1)