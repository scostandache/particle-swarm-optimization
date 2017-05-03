from particle import Particle
import random
from operator import add, sub
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



class Swarm(object):
    # a class to represent a collection of particles

    def __init__(self, pop_size, fitness_func, LIMITS, dim, precision):

        self.POPULATION = [Particle(fitness_func, LIMITS, dim, precision) for _ in xrange(pop_size)]
        self.best_overall_position = self.POPULATION[0].position
        self.best_fitness = self.POPULATION[0].fitness

    def update(self, innertia, cognitive, social):

        for particle in self.POPULATION:

            if particle.fitness < self.best_fitness:
                self.best_overall = particle.position
                self.best_fitness = particle.fitness

            part_one = map(lambda x: x * innertia, particle.velocity)
            part_two = map(lambda x: x * cognitive * random.random(), \
                           map(sub, particle.best_position, particle.position))

            part_three = map(lambda x: x * social * random.random(), \
                           map(sub, self.best_overall_position, particle.position ))

            particle.velocity = map(sum, zip(part_one, part_two, part_three))

            particle.position = map(sum, zip(particle.position, particle.velocity))
            particle.update_fitness()


    def visualize_scatter(self,ax):
        x = np.array([particle.position[0] for particle in self.POPULATION])
        y = np.array([particle.position[1] for particle in self.POPULATION])
        z = [particle.fitness for particle in self.POPULATION]



        ax.scatter(x, y, z, c="r", s=2)

        #trick to maintain the same color of the points in the scatter plot
        #ax.scatter.set_edgecolors = ax.scatter.set_facecolors = lambda *args: None




