import numpy as np

subsystems = 5
redundancy = 5

A = 1
B = 0.0003

def obj_function(r, n):

    total_R = r[0][0] * r[0][3] + r[0][1] * r[0][4] + r[0][1] * r[0][2] * r[0][3] + \
              r[0][0] * r[0][2] * r[0][4] + 2 * r[0][0] * r[0][1] * r[0][2] *\
        r[0][3] * r[0][4] - r[0][1] * r[0][2] * r[0][3] * r[0][4] - r[0][0] * r[0][2] * r[0][3] * r[0][4] - \
        r[0][0] * r[0][1] * r[0][3] * r[0][4] - r[0][0] * r[0][1] * r[0][2] * r[0][4] - r[0][0] * r[0][1] * r[0][2] * r[0][3]

    if total_R >= 0.99:

        solution_quality = np.sum(A * np.exp(B / (1 - r)))

    else:
        solution_quality = 5000  # Penalty

    return -solution_quality
