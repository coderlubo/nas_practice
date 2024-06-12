import random
from utils.settings import INDIVIDUAL_COUNT, INITIAL_POPULATION

def generate_offspring(population):

    offspring = []

    for _ in range(INITIAL_POPULATION):
        # 使用锦标赛选择生成后代种群
        choose = []

        for _ in range(INDIVIDUAL_COUNT):
            
            index = random.randint(0, INITIAL_POPULATION-1)

            # 无 fitness 属性则计算 fitness
            if hasattr(population[index], "fitness") == False:
                population[index].set_fitness()

            choose.append(population[index])

        max_obj = max(choose, key=lambda obj: obj.fitness)

        offspring.append(max_obj)

    return offspring