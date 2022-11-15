import numpy as np

# Redundancy
GEN_ALG = False
BAT_ALG = True
TS_ALG = False

# Reliability
PSO_ALG = False
FA_ALG = True
CS_ALG = False

# RAP
TEN_SYS = False
FIFT_SYS = False

if GEN_ALG:
    from Redundancy_Alg.GA.ga_search_space import gaSpace as redundancySpace
    from Redundancy_Alg.GA.ga_parent import Parent

if BAT_ALG:
    from Redundancy_Alg.BA.ba_search_space import baSpace as redundancySpace
    from Redundancy_Alg.BA.ba_bat import Bat

if TS_ALG:
    from Redundancy_Alg.TS.ts_search_space import tsSpace as redundancySpace
    from Redundancy_Alg.TS.ts_case import Case

if PSO_ALG:
    from Reliability_Alg.PSO.pso_search_space import psoSpace as reliabilitySpace
    from Reliability_Alg.PSO.pso_particle import Particle

if FA_ALG:
    from Reliability_Alg.FA.fa_search_space import faSpace as reliabilitySpace
    from Reliability_Alg.FA.fa_firefly import Firefly

if CS_ALG:
    from Reliability_Alg.CS.cs_search_space import csSpace as reliabilitySpace
    from Reliability_Alg.CS.cs_cuckoo import Cuckoo


class RepetitiveProcedure:
    def __init__(self, max_iterations, population, dimensions, red_upper_bound, fitness):

        self.max_iterations = max_iterations
        self.population = population
        self.dimensions = dimensions

        if GEN_ALG or BAT_ALG or TS_ALG:
            self.red_space = redundancySpace()
            self.red_lower_bound = self.red_space.lower_bound
            self.red_upper_bound = red_upper_bound
            self.red_space.upper_bound = self.red_upper_bound
            self.red_space.dimensions = self.dimensions

        if PSO_ALG or FA_ALG or CS_ALG:
            self.rel_space = reliabilitySpace()
            self.rel_lower_bound = self.rel_space.lower_bound
            self.rel_upper_bound = self.rel_space.upper_bound
            self.rel_space.dimensions = self.dimensions

            self.rel_space.global_best_eval = float('-inf')
            self.rel_space.global_best_redundancy = np.array([0.])
            self.rel_space.global_best_position = np.array([0.])

        # Initialization
        if GEN_ALG:
            self.red_space.parents = [Parent(self.dimensions, self.red_lower_bound, self.red_upper_bound
                                             ) for _ in range(self.population)]
            self.red_space.children = [Parent(self.dimensions, self.red_lower_bound, self.red_upper_bound
                                              ) for _ in range(self.population)]
            self.red_space.fitness = fitness

        elif BAT_ALG:
            self.red_space.bats = [Bat(self.dimensions, self.red_lower_bound, self.red_upper_bound
                                       ) for _ in range(self.population)]
            self.red_space.fitness = fitness

        elif TS_ALG:
            self.red_space.cases = [Case(self.dimensions, self.red_lower_bound, self.red_upper_bound
                                         ) for _ in range(self.population)]
            self.red_space.fitness = fitness

        if PSO_ALG:
            self.rel_space.particles = [Particle(self.dimensions, self.rel_lower_bound, self.rel_upper_bound
                                                 ) for _ in range(self.population)]
            self.rel_space.fitness = fitness

        elif FA_ALG:
            self.rel_space.fireflies = [Firefly(self.dimensions, self.rel_lower_bound, self.rel_upper_bound
                                                ) for _ in range(self.population)]
            self.rel_space.fitness = fitness

        elif CS_ALG:
            self.rel_space.cuckoos = [Cuckoo(self.dimensions, self.rel_lower_bound, self.rel_upper_bound
                                             ) for _ in range(self.population)]
            self.rel_space.fitness = fitness

        elif TEN_SYS:
            tenUnitSys.information = [tenUnitSub() for _ in range(self.population)]

        elif FIFT_SYS:
            fifteenUnitSys.information = [fifteenUnitSub() for _ in range(self.population)]

    def results(self):

        for iteration in range(self.max_iterations):
            if GEN_ALG:
                if PSO_ALG:
                    self.red_space.information = self.rel_space.particles
                elif FA_ALG:
                    self.red_space.information = self.rel_space.fireflies
                elif CS_ALG:
                    self.red_space.information = self.rel_space.cuckoos
                elif TEN_SYS:
                    self.red_space.information = tenUnitSys.information
                elif FIFT_SYS:
                    self.red_space.information = fifteenUnitSys.information
                self.red_space.findTheBestParent()
                self.red_space.crossoverPop()
                self.red_space.tournamentSelection()
                self.red_space.mutation(self.population)

            if BAT_ALG:
                if PSO_ALG:
                    self.red_space.information = self.rel_space.particles
                elif FA_ALG:
                    self.red_space.information = self.rel_space.fireflies
                elif CS_ALG:
                    self.red_space.information = self.rel_space.cuckoos
                elif TEN_SYS:
                    self.red_space.information = tenUnitSys.information
                elif FIFT_SYS:
                    self.red_space.information = fifteenUnitSys.information
                self.red_space.batEvaluation()
                self.red_space.batMovement()

            if TS_ALG:
                if PSO_ALG:
                    self.red_space.information = self.rel_space.particles
                elif FA_ALG:
                    self.red_space.information = self.rel_space.fireflies
                elif CS_ALG:
                    self.red_space.information = self.rel_space.cuckoos
                elif TEN_SYS:
                    self.red_space.information = tenUnitSys.information
                elif FIFT_SYS:
                    self.red_space.information = fifteenUnitSys.information
                self.red_space.caseEvaluation()

            if PSO_ALG:
                if GEN_ALG: self.rel_space.information = self.red_space.parents
                elif BAT_ALG: self.rel_space.information = self.red_space.bats
                elif TS_ALG: self.rel_space.information = self.red_space.cases
                self.rel_space.particleEvaluation()
                self.rel_space.moveParticles()
                self.rel_space.relocation()

            if FA_ALG:
                if GEN_ALG: self.rel_space.information = self.red_space.parents
                elif BAT_ALG: self.rel_space.information = self.red_space.bats
                elif TS_ALG: self.rel_space.information = self.red_space.cases
                self.rel_space.fireflyEvaluation()
                self.rel_space.moveFireflies()
                self.rel_space.relocation()

            if CS_ALG:
                if GEN_ALG: self.rel_space.information = self.red_space.parents
                elif BAT_ALG: self.rel_space.information = self.red_space.bats
                elif TS_ALG: self.rel_space.information = self.red_space.cases
                self.rel_space.cuckooEvaluation()
                self.rel_space.csGlobalMovement()
                self.rel_space.csLocalMovement(self.population)
                self.rel_space.relocation()
        if FIFT_SYS:
            return self.red_space.global_best_eval, self.red_space.global_best_position, fifteenUnitSub().position
        elif TEN_SYS:
            return self.red_space.global_best_eval, self.red_space.global_best_position, tenUnitSub().position
        else:
            return self.rel_space.global_best_eval, self.rel_space.global_best_redundancy, self.rel_space.global_best_position



class tenUnitSys:
    def __init__(self):
        self.information = []

class tenUnitSub:
    def __init__(self):
        self.position = np.array([[0.6796, 0.7329, 0.6688, 0.6102, 0.7911, 0.8140, 0.8088, 0.7142, 0.8487, 0.7901]])

class fifteenUnitSys:
    def __init__(self):
        self.information = []

class fifteenUnitSub:
    def __init__(self):
        self.position = np.array([[0.6796, 0.7329, 0.6688, 0.6102, 0.7911, 0.8140, 0.8088, 0.7142, 0.8487, 0.7901,
                                   0.6972, 0.6262, 0.6314, 0.6941, 0.6010]])