from pso import PSO
import fitness

if __name__ == "__main__":


    PSO = PSO()


    with open('pso_results.txt','w+') as f:
        for function in ['rastrigin','rosenbrock','griewangk']:
            print function
            for no_params in [5,10,30]:
                print no_params
                line =''
                fitness_mean=0.0
                for _ in xrange(20):
                    result = PSO.solve(gen_no=800,
                                       pop_size=250,
                                       fitness=fitness.dispatcher[function]['function'],
                                       LIMITS=fitness.dispatcher[function]['LIMITS'],
                                       dim=no_params,
                                       precision=6,
                                       innertia=0.5,
                                       cognitive=1.2,
                                       social=1.2
                                       )
                    fitness_mean += result
                fitness_mean = fitness_mean / 30.0
                line += function + ' ' + str(no_params) + ' ' + str(fitness_mean) + '\n'
                f.write(line)