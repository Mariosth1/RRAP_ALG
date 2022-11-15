import numpy as np

LOWER_BOUND = 0.5
UPPER_BOUND = 1.


class psoSpace:
    def __init__(self):

        self.fitness = None

        self.lower_bound = LOWER_BOUND
        self.upper_bound = UPPER_BOUND
        self.dimensions = 0

        self.particles = []
        self.information = []

        self.global_best_eval = float('-inf')
        self.global_best_position = np.array([0.])
        self.global_best_redundancy = np.array([0.])

    def particleEvaluation(self):

        # Now I Save the best position and the global best
        i = 0
        for particle in self.particles:

            fitness_eval = self.fitness(particle.position, self.information[i].position)

            # Saving the best position of each particle
            if fitness_eval >= particle.best_position_eval:  # abs if for max and min
                particle.best_position_eval = fitness_eval
                particle.best_position = particle.position

            # Saving global best position
            if fitness_eval >= self.global_best_eval:
                self.global_best_eval = fitness_eval
                self.global_best_position = particle.position
                self.global_best_redundancy = self.information[i].position
                #print(self.global_best_eval, self.global_best_position, self.global_best_redundancy)

            i += 1

    def moveParticles(self):
        W, c1, c2 = 1.5, 1.5, 0.5  # <--- Change them to your desire or use parameter adaptation


        for particle in self.particles:
            new_velocity = (W * particle.velocity) + (
                    c1 * np.random.uniform()) * (particle.best_position - particle.position) + (
                                   c2 * np.random.uniform()) * (self.global_best_position - particle.position)

            particle.velocity = new_velocity
            particle.movement()

    def relocation(self):

        # Relocate the position if it goes out of bounds
        for particle in self.particles:

            for i in range(self.dimensions):

                # Relocation in space
                if particle.position[0][i] > self.upper_bound or particle.position[0][i] < self.lower_bound:

                    particle.position[0][i] = self.lower_bound + (
                            self.upper_bound - self.lower_bound) * np.cos(particle.position[0][i]) ** 2

    # def returnParticles(self):
    #
    #     self.particleEvaluation()
    #     self.moveParticles()
    #     self.relocation()
    #
    #     return self.global_best_position, self.global_best_eval

    # def diversification(self, dimensions, particles_pop):
    #     # Finding the % of exploration
    #     i = 0  # This loop can be done easier, fix it later
    #     for particle in self.particles:
    #         if i == 0: particles_matrix = particle.position
    #         else: particles_matrix = np.concatenate((particles_matrix, particle.position))
    #         i = 1
    #
    #     dim_median = np.median(particles_matrix, axis=0)  # The median of each column(dimension) of the particle matrix
    #
    #     div_in_iter = np.sum(dim_median - particles_matrix) / (particles_pop * dimensions) # Average of Diversity of all dimensions
    #
    #     self.diver_array = np.append(self.diver_array, div_in_iter)
    #
    #     max_diver = np.max((abs(self.diver_array)))
    #     self.diver_per = abs(div_in_iter) / max_diver

