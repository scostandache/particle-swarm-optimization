from pso import PSO
import fitness

if __name__ == "__main__":


    PSO = PSO()
    PSO.solve(gen_no = 100,
              pop_size = 50,
              fitness = fitness.dispatcher['rosenbrock']['function'],
              LIMITS = fitness.dispatcher['rosenbrock']['LIMITS'],
              dim=2,
              precision = 4,
              innertia = 0.8,
              cognitive = 0.7,
              social = 0.95
              )