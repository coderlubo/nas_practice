import numpy as np

from utils.dealCode import init, mutate_code, cross_code
from utils.findBest import find_best
from utils.generateOffspring import generate_offspring
from utils.myIndividual import Individual
from utils.printInfo import print_info
from utils.settings import GENERATE_OFFSPRING_EPOCHS
from utils.testModel import test_model

from utils.globalsVar import set_data, set_logger

logger = set_logger()
train_load, eval_load, test_load = set_data()

print_info()
population = init()

for epoch in range(GENERATE_OFFSPRING_EPOCHS):
    # 到达最后一代
    if epoch == GENERATE_OFFSPRING_EPOCHS - 1:
        break

    # logger.info("Generate {}:\n".format(epoch+1))

    population = generate_offspring(population)

    # 每一代的最优个体
    best_individual = find_best(population)
    # logger.info("\nBest Fitness: \t {}\n".format(best_individual.fitness))
    logger.info("Generate {:<3}: \t Best Fitness: {}".format(epoch+1, best_individual.fitness))

    # 交叉
    for i in range(len(population)-1):

        if i % 2 == 0:

            code1, code2 = cross_code(population[i].code, population[i+1].code)
            population[i] = Individual(code1)
            population[i+1] = Individual(code2)
    
    # 变异
    for i in range(len(population)):

        population[i].code = mutate_code(population[i].code)
        

best_individual = find_best(population)

# 使用测试集进行最终测试
accuracy = test_model(best_individual.model, test_load)

logger.info("Test Accuracy: {}".format(accuracy*100))
logger.info("code: {}".format(best_individual.code))
logger.info(best_individual.model)




            




