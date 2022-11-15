

import numpy as np
from copy import deepcopy

LOWER_BOUND = 1  # This is known for all the RRAP problems

class tsSpace:
    def __init__(self):

        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = 0
        self.dimensions = 0

        self.cases = []
        self.tabu_list = []
        self.tabu_memory = 20
        self.information = []  # Contains agents with agent.position

        self.global_best_eval = float('-inf')
        self.global_best_position = np.ones([1, self.dimensions])

    def caseEvaluation(self):

        i = 0  # counting the population of the information i.e. PSO's agents
        for case in self.cases:

            if case not in self.tabu_list:

                self.tabu_list.append(case)  # Update that the solution has been tested

                fitness_eval = self.fitness(self.information[i].position, case.position)

                # Finding global best position
                if fitness_eval >= self.global_best_eval:
                    self.global_best_eval = fitness_eval
                    self.global_best_position = case.position

            else:

                case.position = np.array(
                        [np.random.randint(self.lower_bound, self.upper_bound) for _ in range(self.dimensions)])


            i += 1  # pop counter

        if len(self.tabu_list) == self.tabu_memory:

            self.tabu_list = []