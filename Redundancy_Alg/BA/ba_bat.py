import numpy as np

class Bat():
    def __init__(self, dimensions, lower_bound, upper_bound):

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimensions = dimensions

        self.position = np.array(
            [np.random.randint(self.lower_bound, self.upper_bound) for _ in range(self.dimensions)])

        self.velocity = np.array([0 for _ in range(self.dimensions)])
        self.frequency = np.array([0 for _ in range(self.dimensions)])  # Temporary
        self.loudness = 1  # Temporary
        self.emission_pulse = 1 # Temporary

        self.prev_pos = self.position

        self.best_position_eval = float('-inf')
