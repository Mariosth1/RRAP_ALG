import numpy as np

subsystems = 4
redundancy = 4


K = [25.0, 25.0, 50.0, 37.5]
A = 1

def obj_function(r, n):

    total_R = 1 - r[0][2] * ((1 - r[0][0]) * (1 - r[0][3])) ** 2 - \
              (1 - r[0][2]) * (1 - r[0][1] * (1 - (1 - r[0][0]) * (1 - r[0][3]))) ** 2

    if total_R >= 0.99:

        solution_quality = np.sum(K * np.tan((np.pi / 2) * r) ** A)

    else:
        solution_quality = 5000  # Penalty

    return -solution_quality