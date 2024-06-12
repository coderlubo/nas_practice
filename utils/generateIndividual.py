import random
from utils.settings import ADD_LAYER_RATE, CONV_LAYER, LINEAR_LAYER, MAX_KERNAL, MAX_LAYERS, MAX_NEURONS, MAX_POOL, MIN_KERNAL, MIN_NEURONS, MIN_POOL, POOLING_LAYER

def generate_neurons():

    return random.randint(MIN_NEURONS, MAX_NEURONS) 

def generate_kernal():

    return random.randint(MIN_KERNAL, MAX_KERNAL)


def generate_conv_layer():

    part = [CONV_LAYER]
    part.append(generate_neurons())
    part.append(generate_kernal())

    return part

def generate_pool_layer():

    part = [POOLING_LAYER]
    part.append(random.randint(MIN_POOL, MAX_POOL))

    return part

def generate_linear_layer():

    part = [LINEAR_LAYER]
    part.append(generate_neurons())

    return part

def generate_individual():

    code = []

    for i in range(MAX_LAYERS):
        if random.uniform(0, 1) < ADD_LAYER_RATE:
            code.extend(generate_conv_layer())
            
            if random.uniform(0, 1) < ADD_LAYER_RATE:
                code.extend(generate_pool_layer())
    
    code.extend(generate_linear_layer())

    return code