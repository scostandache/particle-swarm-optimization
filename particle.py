import random
import copy
class Particle(object):
    # class to respresent a particle in swarm

    def __init__(self, fitness_func, LIMITS, dim, precision):

        if len(LIMITS) == 2:
            assert len(LIMITS) == dim
            self.position = [random.uniform(*LIMITS[0].values()), random.uniform(*LIMITS[1].values())]
        else:
            self.position = [random.uniform(*LIMITS[0].values()) for _ in xrange(dim)]

        self.best_position = copy.deepcopy(self.position)
        self.velocity = [0.0 for _ in self.position]
        self.fitness = round(fitness_func(self.position), precision)
        self.best_fitness = round(fitness_func(self.position), precision)
        self.fitness_func = fitness_func
        self.precision = precision
        self.LIMITS = LIMITS

    def update_fitness(self):

        self.fitness = round(self.fitness_func(self.position), self.precision)

    def normalize_velocity(self, lim):

        for i in xrange(len(self.velocity)):
            if self.velocity[i] > lim:
                self.velocity[i] = lim
            if self.velocity[i] < -lim:
                self.velocity[i] = -lim


    def normalize_position(self):
        if len(self.LIMITS) == 2:
            first_lim = self.LIMITS[0].values()
            second_lim = self.LIMITS[1].values()

            if self.position[0] < first_lim[0] or self.position[1] > first_lim[1]:
                self.position[0] = random.uniform(first_lim[0], first_lim[1])

            if self.position[1] < second_lim[0] or self.position[1] > second_lim[1]:
                self.position[1] = random.uniform(second_lim[0], second_lim[1])

        else:

            limit = self.LIMITS[0].values()

            for i in xrange(len(self.position)):
                if self.position[i] > limit[0] or self.position[i] < limit[1]:
                    print 'old ',self.position[i]
                    self.position[i] = random.uniform(limit[0], limit[1])
                    print 'new ', self.position[i]
