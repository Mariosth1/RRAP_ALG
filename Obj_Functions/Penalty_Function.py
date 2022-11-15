
"----------------------------Penalty Function-----------------------------"
def H_penalty(r, n, v, w, a, b, T, v_bound, w_bound, c_bound):
    import numpy as np

    total_volume = np.sum(v * (n ** 2))
    total_weight = np.sum(w * n * np.exp(n / 4))
    total_cost = np.sum(a * (((-T) / np.log(r)) ** b) * (n + np.exp(n / 4)))


    # "If a constrain is violated H index will be set to 0, else 1"
    # if (total_volume <= v_bound) & (total_weight <= w_bound) & (total_cost <= c_bound):
    #     H = 1
    # else:
    #     H = 0

    PENALTY_PAR = [10 ** (-2.95), 10 ** (-1.5), 10 ** (-2.)]

    H = PENALTY_PAR[0] * max(0, total_cost - c_bound) + \
        PENALTY_PAR[1] * max(0, total_volume - v_bound) + \
        PENALTY_PAR[2] * max(0, total_weight - w_bound)


    if H > 0.005:
        H = 0.25

    return H
