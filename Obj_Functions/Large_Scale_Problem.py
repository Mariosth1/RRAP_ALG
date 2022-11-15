import numpy as np

subsystems = 20
redundancy = 5
# lower_bound = 0.5
# upper_bound = 1
v = np.array([[2.0, 5.0, 5.0, 4.0, 4.0, 1.0, 1.0, 4.0, 4.0, 3.0, 3.0, 1.0, 1.0, 3.0, 4.0, 5.0, 1.0, 4.0, 2.0, 1.0]])
w = np.array([[8.0, 9.0, 6.0, 10.0, 8.0, 9.0, 9.0, 7.0, 9.0, 8.0, 9.0, 8.0, 7.0, 10.0, 6.0, 7.0, 7.0, 8.0, 9.0, 9.0]])
a = np.array([[0.6, 0.1, 1.2, 0.3, 2.9, 1.7, 2.6, 2.5, 1.3, 1.8, 2.4, 1.3, 1.2, 2.1, 0.9, 1.3, 1.9, 2.7, 2.8, 1.5]]) * 10 ** (-5)
b = np.array([[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]])
T = 1000.0
v_bound = 600.0
w_bound = 900.0
c_bound = 700.0

def obj_function(r, n):

    from Obj_Functions.Penalty_Function import H_penalty

    solution_quality = np.prod(1 - (1 - r) ** n) * H_penalty(r, n, v, w, a, b, T, v_bound, w_bound, c_bound)

    return solution_quality