import random
import numpy
import fitness
from operator import add, sub

class Particle(object):
    # class to respresent a particle in swarm

    def __init__(self, fitness_func, LIMITS, dim, precision):

        if len(LIMITS) == 2:
            assert len(LIMITS) == dim
            self.position = [random.uniform(*LIMITS[0].values()), random.uniform(*LIMITS[1].values())]
        else:
            self.position = [random.uniform(*LIMITS[0].values()) for _ in xrange(dim)]

        self.best_position = self.position
        self.velocity = [0.01*x for x in self.position]
        self.fitness = round(fitness_func(self.position), precision)
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



