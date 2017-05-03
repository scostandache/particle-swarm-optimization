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

        fig = plt.figure()
        ax = p3.Axes3D(fig)



        for _ in xrange(gen_no):
            swarm.update(innertia, cognitive, social)
            innertia -= 0.001
            swarm.visualize_scatter(ax)
            print swarm.best_fitness

        ani = animation.FuncAnimation(fig, swarm.visualize_scatter(ax), frames=2000,
                                      interval =1, blit = False, repeat = False)

        plt.show()

