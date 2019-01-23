# class A:
#     def __init__(self):
#         self._internal = 0
#         self.public = 1
#
#     def _internal_method(self):
#         print('internal')
#
#     def public_method(self):
#         print('public')
#
#     def __private_method(self):
#         print('private')
#
#
# s = A()
# print(s.public)
# print(s._internal)
# s._internal_method()
# s.public_method()
# s._A__private_method()


# path = 'text.txt'  # 相对路径
# # path = r'E:\Git\Python3.6'  # windows绝对路径
# # path = 'E:\\Git\\Python3.6'  # windows绝对路径
# # path = r'/home/zhengyx17'  # linux绝对路径
# file = open(path, mode='wb+')
# print(type(file))
# file.write(b'123456\n78901\n')
# # file.writelines(['a', 'b', 'c'])
# # file.flush()
# file.seek(0, 0)
# # file.seek(3, 0)  # 3个偏移量， 0起始位置，1当前位置，2末尾位置
# print(file.readlines())
# print(file.tell())
# print(file.mode)
# print(file.name)
# # file.seek(2, 1)
# # print(file.read())
# file.flush()
# file.close()
# print(file.closed)


# import io
# sio = io.StringIO()
# sio.write('abc')
# sio.seek(0, 0)
# print(sio.read())
# print(sio.tell())
# fw = open('text.txt', 'w')
# print(sio.getvalue(), file=fw)
# sio.close()
# print(sio.closed)

# def login():
#     global single, flag
#     single = 0
#     message = open('login.txt', 'r').read()
#     init_name = eval(message)['name']
#     init_passwd = eval(message)['passwd']
#     flag = eval(message)['state']
#     if int(flag) == 0:
#         print('your account was locked')
#     else:
#         while int(flag):
#             input_name = input('please input your login-name:')
#             input_passwd = input('please input your password:')
#             if input_name == init_name and input_passwd == init_passwd:
#                 print('welcome!')
#                 flag = False
#             else:
#                 single = single + 1
#                 if single == 3:
#                     flag = False
#                     print('your account was locked')
#                     msg = {'name': 'seven', 'passwd': '123', 'state': '0'}
#                     with open('login.txt', 'w') as f:
#                         f.write(str(msg))
#                         f.close()
#                 else:
#                     print('your name or password is not true, you only have %d times'
#                           % (3 - single))
#
#
# login()

# import time
# import io
#
#
# class RunTime:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self.start_time
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_time = time.time()
#         self.run_time = self.end_time - self.start_time
#         print('Time consuming %f' % self.run_time)
#
#
# with RunTime():
#     path = 'text.txt'
#     for i in range(10000):
#         with open(path, 'r') as f:
#             f.read()
#
# with RunTime():
#     for i in range(10000):
#         sio = io.StringIO()
#         sio.write('abc')
#         sio .getvalue()

# import time
#
#
# class RunTime:
#     def __init__(self, name, mode):
#         self.name = name
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.name, mode=self.mode)
#         self.start_time = time.time()
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         self.end_time = time.time()
#         self.run_time = self.end_time - self.start_time
#         print('Time consuming %f' % self.run_time)
#
#
# with RunTime('test.txt', mode='r') as f:
#     print(f)
#     print(f.closed)
# print(f.closed)

# import os
# # os.mkdir('test')
# # os.system('mkdir test1')
# os.system('dir')


# homework
import time
import io


class RunTime:
    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.run_time = self.end_time - self.start_time
        print('Time consuming %f' % self.run_time)


with RunTime():
    with io.StringIO() as sio:
        for _ in range(10000):
            sio.write('1')

with RunTime():
    with open('test.txt', 'w+') as file:
        for _ in range(10000):
            file.write('1')
