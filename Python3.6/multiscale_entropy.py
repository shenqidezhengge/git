import numpy as np


def multiscale_entropy(v, m, r, t):
    """
    calculate the multiscale entropy of time series
    :param v: input raw vector
    :param m: dimension m
    :param r: threshold r * standard deviation
    :param t: scale size
    :return: multiscale entropy
    """
    k = 0
    n = len(v)//t
    s = r * np.std(v)
    w = []
    for i in range(n):
        for j in range(i * t, (i + 1) * t):
            k = k + v[j]
        w.append(k/t)
        k = 0

    U = np.array(w)

    def _maxdist(x_i, x_j):
        result = max([abs(ua - va) for ua, va in zip(x_i, x_j)])
        return result

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for j in range(len(x)) if i != j and _maxdist(x[i], x[j]) <= s]) for i in range(len(x))]
        return sum(C)

    N = len(U)

    phim_1 = _phi(m+1)
    phim = _phi(m)

    if phim and phim_1:
        return -np.log(phim_1 / phim)
    else:
        return np.log(N - m) + np.log(N - m - 1) - np.log(2)


# U = np.array([85, 80, 89] * 17)
# print(SampEn(U, 2, 3))
