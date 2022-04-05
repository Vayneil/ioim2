import math

import data_loader as data
from strain import sigma_p
# def objective():
#     sum = 0
#     for i in range(len(T)):
#         for j in range(len(e[0])):
#             err_squared = (sigma_test[i][j] - sigma_p(a, e[i][j], T[i], e_dot[i])) ** 2
#             err_relative = err_squared / sigma_test[i][j]
#             sum = sum + err_relative
#     return sum


def objective(a):
    result = 0
    delta = 10
    for i in range(data.num_of_experiments):
        for j in range(data.num_of_measurements):
            x, y = sigma_p(a, data.e[i][j], data.e_dot[i], data.T_def[i])
            err_squared = ((data.sigma_test[i][j] - x) ** 2)
            err_relative = err_squared / data.sigma_test[i][j]
            result = result + err_relative
            penalty = 0
            smallest = 1e10
            for k in range(120, 320, 20):
                z, _ = sigma_p(a, k / 100.0, data.e_dot[i], data.T_def[i])
                if z < smallest:
                    smallest = z
            if y > smallest:
                penalty = penalty + delta * math.fabs(y - smallest)
            result = result + penalty
        result = result / data.num_of_measurements
    result = result / data.num_of_experiments
    return result
