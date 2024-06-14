from utils.globalsVar import get_global_logger
from utils.settings import ADD_LAYER_RATE, BATCH_SIZE, CROSS_RATE, DATA_SET, DEVICE, EPOCHS, GENERATE_OFFSPRING_EPOCHS, INDIVIDUAL_COUNT, INITIAL_CHANNEL, INITIAL_POPULATION, MAX_LAYERS, MUTATE_RATE, TRAIN_NAME


def print_info():

    logger = get_global_logger()

    logger.info("TRAIN_NAME: {} \t DATA_SET: {}\n".format(TRAIN_NAME, DATA_SET))\

    logger.info("# Model")
    logger.info("BATCH_SIZE: {} \t EPOCHS: {} \t DEVICE: {} \t INITIAL_CHANNEL: {}\n".format(BATCH_SIZE, EPOCHS, DEVICE, INITIAL_CHANNEL))


    logger.info("# 进化算法")
    logger.info("GENERATE_OFFSPRING_EPOCHS: {} \t INITIAL_POPULATION: {} \t INDIVIDUAL_COUNT: {}\n".format(GENERATE_OFFSPRING_EPOCHS, INITIAL_POPULATION, INDIVIDUAL_COUNT))

    logger.info("# 概率")
    logger.info("ADD_LAYER_RATE: {} \t CROSS_RATE: {} \t MUTATE_RATE: {}\n".format(ADD_LAYER_RATE, CROSS_RATE, MUTATE_RATE))

    logger.info("# 编码模型")
    logger.info("MAX_LAYERS: {}\n".format(MAX_LAYERS))