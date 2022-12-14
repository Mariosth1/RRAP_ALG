import numpy as np

class Cuckoo():
    def __init__(self, dimensions, lower_bound, upper_bound):

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimensions = dimensions
        self.position = np.array(
            [[(lower_bound + (upper_bound - lower_bound)*np.random.uniform()) for _ in range(self.dimensions)]])
        self.best_position = self.position
        self.best_position_eval = float('-inf')