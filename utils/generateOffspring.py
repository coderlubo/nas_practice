import random
from utils.settings import INDIVIDUAL_COUNT, INITIAL_POPULATION



def generate_offspring(population, train_load, eval_load):

    offspring = []

    for _ in range(INITIAL_POPULATION):
        # 使用锦标赛选择生成后代种群
        choose = []

        for _ in range(INDIVIDUAL_COUNT):
            index = random.randint(0, INITIAL_POPULATION)

            # 无 fitness 属性则计算 fitness
            if hasattr(population[index], "fitness") == False:
                population[index].set_fitness(train_load, eval_load)

            choose.append(population[index])

        max_obj = max(choose, key=lambda obj: obj.fitness)

        offspring.append(max_obj)

    return offspring