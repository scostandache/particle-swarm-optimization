from pso import PSO
import fitness

if __name__ == "__main__":


    PSO = PSO()
    PSO.solve(gen_no = 1000,
              pop_size = 250,
              fitness = fitness.dispatcher['rastrigin']['function'],
              LIMITS = fitness.dispatcher['rastrigin']['LIMITS'],
              dim=30,
              precision = 9,
              innertia = 0.7,
              cognitive = 1.4,
              social = 1.4
              )