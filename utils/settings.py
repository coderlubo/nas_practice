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


# 概率
ADD_LAYER_RATE = 1
CROSS_RATE = .5
MUTATE_RATE = .5


# Model
BATCH_SIZE = 64
EPOCHS = 20
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


# 进化算法
INITIAL_POPULATION = 10