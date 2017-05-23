from particle import Particle
import random
import numpy as np


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

            new_velocity = [0.0 for _ in particle.velocity]

            first_rand = random.random()
            second_rand = random.random()

            for i in xrange(len(particle.velocity)):
                part_one = innertia * particle.velocity[i]
                part_two = cognitive * random.random() * \
                           (particle.best_position[i] - particle.position[i])
                part_three = social * random.random() * \
                             (self.best_overall_position[i] - particle.position[i])
                new_velocity[i] = part_one + part_two + part_three

            particle.velocity = new_velocity

            particle.normalize_velocity(2.0)

            new_position = map(sum, zip(particle.position, particle.velocity))

            particle.position = new_position

            particle.normalize_position()

            particle.update_fitness()


            if particle.fitness < particle.best_fitness:
                particle.best_position = particle.position
                particle.best_fitness = particle.fitness

            if particle.best_fitness < self.best_fitness:
                self.best_overall_position = particle.best_position
                self.best_fitness = particle.best_fitness

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
