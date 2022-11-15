import numpy as np
from copy import deepcopy

LOWER_BOUND = 1

class gaSpace:
    def __init__(self):

        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = 0
        self.dimensions = 0

        self.parents = []
        self.children = []
        self.information = []  # Contains agents with agent.position

        self.global_best_eval = float('-inf')
        self.global_best_position = np.ones([1, self.dimensions])

        self.ga_mutation = 0.005

    def findTheBestParent(self):

        # Find the best parent
        i = 0  # counting the population of the information i.e. PSO's agents
        for parent in self.parents:

            fitness_eval = self.fitness(self.information[i].position, parent.position)

            # Finding global best position
            if fitness_eval >= self.global_best_eval:
                self.global_best_eval = fitness_eval
                self.global_best_position = parent.position

            i += 1  # pop counter

    def crossoverPop(self):

        ga_crossover = np.random.randint(1, self.dimensions)

        i = 0
        for parent in self.parents:

            child = np.append(self.global_best_position[:ga_crossover], parent.position[ga_crossover:])
            self.children[i].position = child

            i += 1

    def tournamentSelection(self):

        pop_size = 0
        parents_quality = []
        children_quality = []
        for parent in self.parents:
            parents_quality.append(self.fitness(self.information[pop_size].position, parent.position))
            children_quality.append(self.fitness(self.information[pop_size].position, self.children[pop_size].position))
            pop_size += 1  # i can pass it in the function, but counting it in here in case i want to increase it

        new_pop_quality = np.array([parents_quality + children_quality])

        # Finding the population_size best indexes, so that the pop size is the same
        temp = deepcopy(new_pop_quality)  # Temporarily find the population_size best qualities

        order = temp.argsort()
        ranks = order.argsort()
        new_pop = np.append(self.parents, self.children)

        self.parents = []

        i = 0
        for parent in new_pop:

            if ranks[0][i] < pop_size:
                self.parents = np.append(self.parents, parent)

            i += 1

    def mutation(self, pop_size):
        par_portion = int(np.ceil(pop_size / 15))

        # Choose a portion of parents and randomly mutate them
        if np.random.random() < self.ga_mutation:

            for _ in range(par_portion):

                rand_par = np.random.randint(0, pop_size)

                self.parents[rand_par].position = np.array(
            [np.random.randint(self.lower_bound, self.upper_bound) for _ in range(self.dimensions)])