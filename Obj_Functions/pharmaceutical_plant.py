import numpy as np

subsystems = 10
redundancy = 5
# lower_bound = 0.5
# upper_bound = 1
v = np.array([4.0, 5.0, 3.0, 2.0, 3.0, 4.0, 1.0, 1.0, 4.0, 4.0])
w = np.array([9.0, 7.0, 5.0, 9.0, 9.0, 10.0, 6.0, 5.0, 8.0, 6.0])
a = np.array([0.611360, 4.032464, 3.578225, 3.654303, 1.163718, 2.966955, 2.045865, 2.649522, 1.982908, 3.516724]) * 10 ** (-5)
b = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
T = 1000.0
v_bound = 289.0
w_bound = 483.0
c_bound = 553.0


def obj_function(r, n):
    from Obj_Functions.Penalty_Function import H_penalty

    R = (1 - (1 - r) ** n)

    solution_quality = np.prod(R) * H_penalty(r, n, v, w, a, b, T, v_bound, w_bound, c_bound)

    return solution_quality
