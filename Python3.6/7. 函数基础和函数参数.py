


def func(x):
    print(x)


def func1(x, y=None):
    print(x)
    print(y)


def func2(*args, **kwargs):
    print(args)
    print(kwargs)


print('func')
func(1)
print('func1')
func1(1)
func1(1, 2)
print('func2')
func2(1, 2, 3, a=4, b=5, c=6)
func2(*(1, 2, 3), **{'a': 4, 'b': 5, 'c': 6})
func2(1, 2, 3)
