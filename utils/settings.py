import time
import torch


MAX_LAYERS = 5

MAX_NEURONS = 128
MIN_NEURONS = 16

MAX_KERNAL = 5
MIN_KERNAL = 2

MAX_POOL = 3
MIN_POOL = 2


CONV_LAYER = -1
CONV_LAYER_LEN = 3

POOLING_LAYER = -2
POOLING_LAYER_LEN = 2

LINEAR_LAYER = -3
LINEAR_LAYER_LEN = 2

# Model
BATCH_SIZE = 64
EPOCHS = 20
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


# 进化算法
GENERATE_OFFSPRING_EPOCHS = 10
INITIAL_POPULATION = 20
INDIVIDUAL_COUNT = 5    # 锦标赛个体数量

# 概率
ADD_LAYER_RATE = .5
CROSS_RATE = .5
MUTATE_RATE = .1



LOGGER_PATH = "./logs/" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.log'