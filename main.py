from utils.dealCode import cross_code, init, mutate_code
from utils.findBest import find_best
from utils.generateOffspring import generate_offspring
from utils.getData import get_data
from utils.myLog import get_logger
from utils.settings import CROSS_RATE, GENERATE_OFFSPRING_EPOCHS, INITIAL_POPULATION, MUTATE_RATE
from utils.testModel import test_model


logger = get_logger()
train_load, eval_load, test_load = get_data()


population = init()


for i in range(GENERATE_OFFSPRING_EPOCHS):
    logger.info("Generate {}:".format(i+1))

    offspring = generate_offspring(population, train_load, eval_load)

    # 每一代的最优个体
    best_individual = find_best(offspring, train_load, eval_load)
    logger.info("Best Fitness: \t {}".format(best_individual.fitness))

    # 到达最后一代
    if i == GENERATE_OFFSPRING_EPOCHS - 1:
        break

    # 交叉
    for i in range(len(offspring)):

        if i % 2 == 0:
            offspring[i].code, offspring[i+1].code = cross_code(offspring[i].code, offspring[i+1].code)
            del offspring[i].fitness
            del offspring[i+1].fitness

    
    # 变异
    for i in range(len(offspring)):

            offspring[i].code = mutate_code(offspring[i].code)
            del offspring[i+1].fitness

best_individual = find_best(offspring)

# 使用测试集进行最终测试
accuracy = test_model(best_individual.model, test_load)

logger.info("Test Accuracy: {}".format(accuracy*100))




            




