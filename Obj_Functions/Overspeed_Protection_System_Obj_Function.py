import numpy as np

subsystems = 4
redundancy = 10
# lower_bound = 0.5
# upper_bound = 1
v = np.array([1.0, 2.0, 3.0, 2.0])
w = np.array([6.0, 6.0, 8.0, 7.0])
a = np.array([1.0, 2.3, 0.3, 2.3]) * 10 ** (-5)
b = np.array([1.5, 1.5, 1.5, 1.5])
T = 1000.0
v_bound = 250.0
w_bound = 500.0
c_bound = 400.0


def obj_function(r, n):
    from Obj_Functions.Penalty_Function import H_penalty

    R = (1 - (1 - r) ** n)

    solution_quality = np.prod(R) * H_penalty(r, n, v, w, a, b, T, v_bound, w_bound, c_bound)

    return solution_quality
