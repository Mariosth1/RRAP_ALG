
import numpy as np
from copy import deepcopy

LOWER_BOUND = 1
UPPER_BOUND = 5

DIMENSIONS = 5  # Temporary


class baSpace():
    def __init__(self):


        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = UPPER_BOUND
        self.dimensions = DIMENSIONS

        self.bats = []
        self.information = []  # Contains agents with agent.position

        self.global_best_eval = float('-inf')
        self.global_best_position = np.ones(self.dimensions)

        # Parameters
        self.alpha = 1  # Cooling Factor like Simulated Annealing
        self.gamma = 1  # Need to find what this is
        self.emission_pulse0 = 0.25 # Temporary
        self.loudness0 = 8  # Temporary
        self.frequency_max = 8  # Temporary
        self.frequency_min = 2  # Temporary


        self.gen_counter = 1

    def batEvaluation(self):

        # Now I Save the best position and the global best
        i = 0
        for bat in self.bats:

            fitness_eval = self.fitness(self.information[i].position, bat.position)

            # Saving global best position
            if fitness_eval >= self.global_best_eval:
                self.global_best_eval = fitness_eval
                self.global_best_position = bat.position

            i += 1

    def batMovement(self):

        # Assign Frequency and Velocity
        pop_i = 0
        for bat in self.bats:

            bat.prev_pos = deepcopy(bat.position)

            bat.frequency = self.frequency_min * (
                    self.frequency_max - self.frequency_min) * np.random.uniform(0, 1, self.dimensions)

            bat.velocity = bat.velocity + (bat.position - self.global_best_position) * bat.frequency

            for j in range(self.dimensions):

                ar_rand = np.random.uniform()
                if ar_rand < np.abs((2 / np.pi) * np.arctan(2 / np.pi) * bat.velocity[j]):

                    bat.position[j] = self.global_best_position[j] + np.random.randint(-1, 2)  # [-1, 0, 1]
                    # I can relocate here
                elif ar_rand > bat.emission_pulse:

                    bat.position[j] = self.global_best_position[j]

            self.relocation()

            if not(self.fitness(self.information[pop_i].position, bat.position
                            ) > self.fitness(self.information[pop_i].position, bat.prev_pos) and ar_rand < bat.loudness):

                bat.position = deepcopy(bat.prev_pos)

            # Update Loudness and pulse rate

            # if the new position is feasible then the solution wont be equal to 0 (due to penalty)
            if self.fitness(self.information[pop_i].position, bat.position) != 0:

                bat.loudness = self.loudness0
                bat.emission_pulse = self.emission_pulse0
                self.gen_counter = 1

            else:
                bat.loudness *= self.alpha
                bat.emission_pulse = self.emission_pulse0 * (1 - np.exp(-self.gamma * self.gen_counter))

            self.gen_counter += 1
            pop_i += 1

    def relocation(self):

        for bat in self.bats:

            for j in range(self.dimensions):

                if bat.position[j] > self.upper_bound: bat.position[j] = self.upper_bound
                elif bat.position[j] < self.lower_bound: bat.position[j] = self.lower_bound
                else: pass
