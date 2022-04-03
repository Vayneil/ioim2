import math
import data_loader as data
# def sigma_p(a, e, T, e_dot):
#     R = 8.314
#     W = math.exp(-a[6] * e)
#     T1 = math.exp(a[3] / (R * (T + 273)))
#     T2 = math.exp(a[5] / (R * (T + 273)))
#     e1 = e ** a[1]
#     edot1 = e_dot ** a[2]
#     result = W * a[0] * T1 * e1
#     result = result + ((1 - W) * a[4] * T2)
#     result = result * edot1
#     return result


def sigma_p(e, e_dot, T):
    Z = data.e_dot * math.exp(data.q_def * data.R_gas * data.T_def)
    sigma0 = 1 / data.a[2] * (1 / math.sinh(Z / data.a[0]) ** (1 / data.a[1]))
    sigma_sse = 1 / data.a[5] * (1 / math.sinh(Z / data.a[3]) ** (1 / data.a[4]))
    sigma_ss = 1 / data.a[10] * (1 / math.sinh(Z / data.a[8]) ** (1 / data.a[9]))
    e_r = (data.a[6] + data.a[7] * sigma_sse ** 2) / 3.23
    e_xsc = data.a[13] * (Z / sigma_sse ** 2) ** data.a[14]
    e_xrc = e_xsc / 1.98
    e_c = data.a[11] * (Z / sigma_sse ** 2) ** data.a[12]
    R = 0
    if data.e > e_c:
        R = (sigma_sse - sigma_ss) * (1 - math.exp(-((data.e - e_c) / e_xrc) ** 2))
    return sigma0 + (sigma_sse - sigma0) * math.sqrt(1 - math.exp(-data.e / e_r)) - R
