# author shenqidezhengge 2018/11/20

# 找到矩阵的最大特征值
'''
from numpy import mat,linalg,sqrt
import math
A = mat([[-1, 2, -3],[4, -6, 6]])
B = A.T
a,b = linalg.eig(B*A)
a.sort()
a = sqrt(a)
print(a[2])
'''

# 尝试求随机数组相关系数
# 接近0
'''
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
a = frame.iloc[::2] = np.nan
b = frame['a'].corr(frame['b'])
c = frame['a'].corr(frame['b'], method='spearman')
d = frame.corr()
f = 1
'''

# 计算相关系数
# 接近1或-1

import numpy as np
import pandas as pd
c = np.random.randn(8)
a = pd.Series(np.array((1, 2, 3, 4, 5)))
# b = pd.Series(np.array((2, 3, 4, 5, 6)))
b = pd.Series(np.array((6, 5, 4, 3, 2)))
var_a = a.var()
print(var_a)
var_b = b.var()
print(var_b)
cov = a.cov(b)
print(cov)
corr = a.corr(b)
print(corr)


