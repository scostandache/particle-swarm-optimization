from pso import PSO
import fitness

if __name__ == "__main__":


    PSO = PSO()
    PSO.solve(gen_no = 10000,
              pop_size = 450,
              fitness = fitness.dispatcher['rastrigin']['function'],
              LIMITS = fitness.dispatcher['rastrigin']['LIMITS'],
              dim=20,
              precision = 8,
              innertia = 1.0,
              cognitive = 2.0,
              social = 2.0
              )