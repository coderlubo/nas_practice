import copy
import random
from utils.globalsVar import get_global_logger
from utils.myIndividual import Individual
from utils.settings import INDIVIDUAL_COUNT, INITIAL_POPULATION

logger = get_global_logger()

def generate_offspring(population):

    offspring = []

    for _ in range(INITIAL_POPULATION):
        # 使用锦标赛选择生成后代种群
        choose = []

        for _ in range(INDIVIDUAL_COUNT):
            
            index = random.randint(0, INITIAL_POPULATION-1)

            # 无 fitness 属性则计算 fitness
            if hasattr(population[index], "fitness") == False:
                try:
                    population[index].set_fitness()

                except Exception as e:

                    population[index].fitness = 0
                    

            choose.append(population[index])

        max_obj = max(choose, key=lambda obj: obj.fitness)

        offspring.append(copy.deepcopy(max_obj))

    

    # 使用轮盘赌生成后代种群
    # total_fitness = 0

    # for i in range(len(population)):
    #     if hasattr(population[i], "fitness") == False:
    #         population[i].set_fitness()
        
    #     total_fitness += population[i].fitness

    # # 每个个体对应的概率
    # rate_arr = [individual.fitness/total_fitness for individual in population]

    # # 累积概率
    # total_rate = [sum(rate_arr[:i+1]) for i in range(len(rate_arr))]

    # for i in range(INITIAL_POPULATION):
    #     rate_random = random.uniform(0, 1)

    #     for index, rate in enumerate(total_rate):
    #         if rate_random <= rate:
    #             offspring.append(copy.deepcopy(population[index]))
    #             break

    return offspring