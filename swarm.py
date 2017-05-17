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
        self.LIMITS = LIMITS
        self.fitness_func = fitness_func

    def update(self, innertia, cognitive, social):

        for particle in self.POPULATION:

            new_velocity = [0.0 for _ in xrange(len(particle.velocity))]

            first_rand = random.random()
            second_rand = random.random()

            for i in xrange(len(particle.velocity)):
                part_one = innertia * particle.velocity[i]
                part_two = cognitive * first_rand * \
                           (particle.best_position[i] - particle.position[i])
                part_three = social * second_rand * \
                             (self.best_overall_position[i] - particle.position[i])
                new_velocity[i] = part_one + part_two + part_three

            particle.velocity = new_velocity
            particle.normalize_velocity(2.0)

            new_position = map(sum, zip(particle.position, particle.velocity))

            if len(self.LIMITS) == 2:
                first_lim = self.LIMITS[0].values()
                second_lim = self.LIMITS[1].values()

                if new_position[0] < first_lim[0] or new_position[1] > first_lim[1]:
                    new_position[0] = random.uniform(first_lim[0], first_lim[1])
                    # print 'found'
                if new_position[1] < second_lim[0] or new_position[1] > second_lim[1]:
                    new_position[1] = random.uniform(second_lim[0], second_lim[1])

            else:

                limit = self.LIMITS[0].values()
                # print particle.position, particle.fitness
                for i in xrange(len(new_position)):
                    if new_position[i] < limit[0] or new_position[i] > limit[1]:
                        new_position[i] = random.uniform(limit[0], limit[1])
                        # print 'updated'



            if (self.fitness_func(new_position) < particle.fitness):
                particle.best_position = new_position
                particle.position = new_position
                # particle.update_fitness()

            particle.update_fitness()
            # print particle.position, particle.fitness, '\n'

            if particle.fitness < self.best_fitness:
                self.best_overall = particle.position
                self.best_fitness = particle.fitness

    def visualize_scatter(self):
        x = np.array([particle.position[0] for particle in self.POPULATION])
        y = np.array([particle.position[1] for particle in self.POPULATION])
        z = [particle.fitness for particle in self.POPULATION]


        # ax = fig.gca(projection='3d')
        # s = ax.scatter(x, y, z, c="r", s=2)
        #
        # # trick to maintain the same color of the points in the scatter plot
        # s.set_edgecolors = s.set_facecolors = lambda *args: None
        #
        # ax.legend()
        #
        # ax.set_xlabel('first argument')
        # ax.set_ylabel('second argument')
        # ax.set_zlabel('fitness')
