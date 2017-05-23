from swarm import Swarm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import time
import numpy as np

class PSO(object):

    def solve(self,
              gen_no,
              pop_size,
              fitness,
              LIMITS,
              dim,
              precision,
              innertia,
              cognitive,
              social):

        swarm = Swarm(pop_size, fitness, LIMITS, dim, precision)

        # for i in xrange(gen_no):
        #     swarm.update(innertia, cognitive, social)
        #     innertia -= 0.01
        #     print swarm.best_fitness

# ============================

        x = np.array([])
        y = np.array([])
        z = np.array([])
        count = 0
        best_color = np.array([])

        def update_graph(count):

            x = np.array([particle.position[0] for particle in swarm.POPULATION])
            y = np.array([particle.position[1] for particle in swarm.POPULATION])
            z = [particle.fitness for particle in swarm.POPULATION]

            graph.set_data(x, y)
            graph.set_3d_properties(z)

            ax.set_xlim3d(tuple(LIMITS[0].values()))
            ax.set_ylim3d(tuple(LIMITS[0].values()))
            ax.set_zlim3d(min([particle.fitness for particle in swarm.POPULATION]) - 3,
                          max([particle.fitness for particle in swarm.POPULATION]) + 3)

            swarm.update(innertia, cognitive, social)

            title.set_text('function = {}, '
                           'time={}, '
                           'best_found = {}'
                           .format(fitness.__name__, count, swarm.best_fitness))
            return title, graph,


        fig = plt.figure()

        ax = fig.add_subplot(111, projection = '3d')

        ax.set_xlabel('first argument')
        ax.set_ylabel('second argument')
        ax.set_zlabel('fitness')

        title = ax.set_title('')
        graph, = ax.plot(xs=x, ys=y, zs=z, linestyle="", marker=".", color='k', c=best_color)
        ani = animation.FuncAnimation(fig, update_graph, gen_no, interval=1, blit = True, repeat=True,  repeat_delay= 5000)

        plt.show()


