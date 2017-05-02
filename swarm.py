from particle import Particle


class Swarm(object):
    # a class to represent a collection of particles

    def __init__(self, pop_size, fitness, LIMITS, dim):

        self.POPULATION = [Particle(fitness, LIMITS, dim) for _ in xrange(pop_size)]
        self.best_overall = self.POPULATION[0]
        self.best_fitness = self.POPULATION[0].fitness

    def update(self, innertia, cognitive, social):

        for particle in self.POPULATION:

            if particle.fitness < self.best_fitness:
                self.best_overall = particle.position
                self.best_fitness = particle.fitness

