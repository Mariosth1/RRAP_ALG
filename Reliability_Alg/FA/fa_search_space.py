
import numpy as np

LOWER_BOUND = 0.5
UPPER_BOUND = 1.


class faSpace:
    def __init__(self):

        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = UPPER_BOUND
        self.dimensions = 0

        self.fireflies = []
        self.information = []

        self.global_best_eval = float('-inf')
        self.global_best_position = np.array([0.])
        self.global_best_redundancy = np.array([0.])

        self.alpha = 0.2

    def fireflyEvaluation(self):

        # Now I Save the best position and the global best
        i = 0
        for firefly in self.fireflies:

            fitness_eval = self.fitness(firefly.position, self.information[i].position)
            firefly.position_eval = fitness_eval

            # Saving the best position of each particle
            if fitness_eval >= firefly.best_position_eval:  # abs if for max and min
                firefly.best_position_eval = fitness_eval
                firefly.best_position = firefly.position

            # Saving global best position
            if fitness_eval >= self.global_best_eval:
                self.global_best_eval = fitness_eval
                self.global_best_position = firefly.position
                self.global_best_redundancy = self.information[i].position

            i += 1

    def moveFireflies(self):

        # Parameters
        self.alpha *= 0.98  # delta
        gamma = 1 # <--- Change them to your desire or use parameter adaptation
        beta0 = 1

        for i in range(len(self.fireflies)):

            dimensions = self.fireflies[i].position.shape[1]

            for j in range(len(self.fireflies)):

                if self.fireflies[i].position_eval < self.fireflies[j].position_eval and i != j:

                    r_dist = self.fireflies[j].position - self.fireflies[i].position
                    # new_light = β beta
                    new_light_attract = beta0 * np.exp(
                        -gamma * r_dist ** 2) * r_dist + self.alpha * np.random.uniform(0, 1, [1, dimensions])

                    self.fireflies[i].light_attract = new_light_attract
                    self.fireflies[i].movement()

    def relocation(self):

        # Relocate the position if it goes out of bounds
        for firefly in self.fireflies:

            for i in range(self.dimensions):

                # Relocation in space
                if firefly.position[0][i] > self.upper_bound or firefly.position[0][i] < self.lower_bound:

                    firefly.position[0][i] = self.lower_bound + (
                            self.upper_bound - self.lower_bound) * np.cos(firefly.position[0][i]) ** 2