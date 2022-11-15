import numpy as np
from copy import deepcopy

LOWER_BOUND = 0.5
UPPER_BOUND = 1.0


class csSpace():
    def __init__(self):

        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = UPPER_BOUND
        self.dimensions = 0

        self.cuckoos = []
        self.information = []

        self.global_best_eval = float('-inf')
        self.global_best_position = np.array([0.])
        self.global_best_redundancy = np.array([0.])

        # Parameters
        self.scaling_factor = 0.01  # O(L/100) or O(L/10)
        self.sigma = 0.5  # step_size

    def cuckooEvaluation(self):

        # Now I Save the best position and the global best
        i = 0
        for cuckoo in self.cuckoos:

            fitness_eval = self.fitness(cuckoo.position, self.information[i].position)

            # Saving the best position of each particle
            if fitness_eval >= cuckoo.best_position_eval:  # abs if for max and min
                cuckoo.best_position_eval = fitness_eval
                cuckoo.best_position = cuckoo.position

            # Saving global best position
            if fitness_eval >= self.global_best_eval:
                self.global_best_eval = fitness_eval
                self.global_best_position = cuckoo.position
                self.global_best_redundancy = self.information[i].position

            i += 1

    def csGlobalMovement(self):

        pop_size = 0
        cuckoos_quality = []

        for cuckoo in self.cuckoos:

            cuckoos_quality.append(self.fitness(cuckoo.position, self.information[pop_size].position))
            pop_size += 1

        cuckoos_quality = np.array([cuckoos_quality])
        order = cuckoos_quality.argsort()
        ranks = order.argsort()

        i = 0
        for cuckoo in self.cuckoos:

            if ranks[0][i] > pop_size:
                lev_lambda = 1.5
                levy = (lev_lambda * np.random.gamma(lev_lambda) * np.sin(np.pi * lev_lambda / 2)) / (
                        np.pi * self.sigma ** (1 + lev_lambda))

                cuckoo.position = cuckoo.position + self.scaling_factor * levy

            i += 1

    def csLocalMovement(self, pop_size):

        # Pa switching parameter
        switch_par = 0.25

        i = 0
        for cuckoo in self.cuckoos:

            cuckoo.position = cuckoo.position + self.scaling_factor * self.sigma * \
                              np.heaviside(switch_par - np.random.uniform(), 1) * \
                                           (self.cuckoos[np.random.randint(1, pop_size)].position - \
                                            self.cuckoos[np.random.randint(1, pop_size)].position)

            i += 1

    def relocation(self):

        # Relocate the position if it goes out of bounds
        for cuckoo in self.cuckoos:

            for i in range(self.dimensions):

                # Relocation in space
                if cuckoo.position[0][i] > self.upper_bound or cuckoo.position[0][i] < self.lower_bound:

                    cuckoo.position[0][i] = self.lower_bound + (
                            self.upper_bound - self.lower_bound) * np.cos(cuckoo.position[0][i]) ** 2