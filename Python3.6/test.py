# # 内置函数排序
# def my_sorted(a, reverse=False):
#     if not reverse:
#         return list(sorted(a))
#     elif reverse:
#         return list(reversed(sorted(a)))
#     else:
#         return 'Wrong Input'
#
#
# # 选择法排序
# def my_sorted1(a, reverse=False):
#     for i in range(len(a) - 1):
#         i_min = i
#         for j in range(i, len(a)):
#             if not reverse and a[j] < a[i_min] or reverse and a[j] > a[i_min]:
#                 i_min = j
#         t = a[i]
#         a[i] = a[i_min]
#         a[i_min] = t
#     return a
#
#
# # 冒泡法排序
# def my_sorted2(a, reverse=False):
#     for i in range(len(a) - 1):
#         for j in range(len(a) - i - 1):
#             if a[j] > a[j + 1] and not reverse or a[j] < a[j + 1] and reverse:
#                 t = a[j]
#                 a[j] = a[j + 1]
#                 a[j + 1] = t
#     return a
#
#
# b = [3, 2, 4, 3, 1, 9, 3, 8, 7, 5, 6]
# print('my_sorted()')
# print(my_sorted(b))
# print(my_sorted(b, True))
# print('my_sorted1()')
# print(my_sorted1(b))
# print(my_sorted1(b, True))
# print('my_sorted2()')
# print(my_sorted2(b))
# print(my_sorted2(b, True))

# import numpy as np
# test = np.load('data216x197.npy', encoding="latin1")  # 加载文件
# doc = open('1.txt', 'a')  # 打开一个存储文件，并依次写入
# print(test, file=doc)  # 将打印内容写入文件中


# import numpy as np
# fr = open('multiscale_entropy_of_flows.txt')
# line_arr = []
# for line in fr.readlines():
#     tmp = line.strip().split('\t')
#     for i in range(6):
#         tmp[i] = float('{:.5}'.format(tmp[i]))
#     line_arr.append(tmp)
# print(line_arr)
# np.save('mse_of_flows.npy', line_arr)
# c = np.load('mse_of_flows.npy')
# print(c)

# from svmutil import *
# y, x = svm_read_problem('mse_data1.txt')
# # m = svm_train(y[:56], x[:56], '-t 2 -c 675 -g 1.74')
# m = svm_train(y[:56], x[:56])
# p_label, p_acc, p_val = svm_predict(y[56:], x[56:], m)
# # print(p_label)
# # print(p_acc)
# # print(p_val)
# print('real label\tpredicted label')
# for i in range(len(p_label)):
#     print('{}\t\t\t{}'.format(y[i + 56], p_label[i]))


# def main():
#     print('Hello World!')
#
#
# main()

# print(format(4, '#b'))
#
# print(f'{14:#b}')


def sum_two_numbers(a: int, b: int) -> int:
    return a + b


print(sum_two_numbers(1, 9))

