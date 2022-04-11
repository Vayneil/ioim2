import data_loader as data
from strain import sigma_p
import math

# SIM 1
# def objective():
#     sum = 0
#     for i in range(len(T)):
#         for j in range(len(e[0])):
#             err_squared = (sigma_test[i][j] - sigma_p(a, e[i][j], T[i], e_dot[i])) ** 2
#             err_relative = err_squared / sigma_test[i][j]
#             sum = sum + err_relative
#     return sum


# SIM 2
def objective():
    result = 0
    delta = 10
    for i in range(data.num_of_experiments):
        for j in range(data.num_of_measurements):
            a, b = sigma_p(data.e[i][j], data.T_def[i], data.e_dot[i])
            err_squared = ((data.sigma_test[i][j] - a) ** 2)
            err_relative = err_squared / data.sigma_test[i][j]
            result = result + err_relative
            highest = 1E10
            for k in range(125, 300, 25):
                sigma, _ = sigma_p(data.e[i][j], data.T_def[i], k / 100.0)
                if sigma < highest:
                    highest = sigma
                    print(k)
            print(highest)
            print(b)
            if highest < b:
                delta * math.fabs(b - highest)
    print(result / data.num_of_experiments / data.num_of_measurements)
    return result / data.num_of_experiments / data.num_of_measurements


objective()
