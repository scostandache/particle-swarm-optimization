from pso import PSO
import fitness

if __name__ == "__main__":


    PSO = PSO()
    PSO.solve(gen_no = 10000,
              pop_size = 250,
              fitness = fitness.dispatcher['rastrigin']['function'],
              LIMITS = fitness.dispatcher['rastrigin']['LIMITS'],
              dim=2,
              precision = 8,
              innertia = 1,
              cognitive = 2.0,
              social = 2.0
              )