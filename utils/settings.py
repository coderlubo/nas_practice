import time
import torch


# 数据集 MNIST、CIFAR10
DATA_SET = "CIFAR10"

# Model
BATCH_SIZE = 64
EPOCHS = 10
DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'
INITIAL_CHANNEL = 3


# 进化算法
GENERATE_OFFSPRING_EPOCHS = 500
INITIAL_POPULATION = 100
INDIVIDUAL_COUNT = 10   # 锦标赛个体数量

# 概率
ADD_LAYER_RATE = .5
CROSS_RATE = .7
MUTATE_RATE = .1

LOGGER_PATH = "./logs/" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.log'

# 编码模型
MAX_LAYERS = 6

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