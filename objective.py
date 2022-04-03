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


def objective():
    result = 0
    for i in range(data.num_of_experiments):
        for j in range(data.num_of_measurements):
            err_squared = ((data.sigma_test[i][j] - sigma_p(data.e[i][j], data.T_def[i], data.e_dot[i])) ** 2)
            err_relative = err_squared / data.sigma_test[i][j]
            result = result + err_relative
    return result / data.num_of_experiments / data.num_of_measurements
