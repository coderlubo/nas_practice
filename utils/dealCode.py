import random
from utils.generateIndividual import generate_individual
from utils.myIndividual import Individual
from utils.settings import CONV_LAYER, CONV_LAYER_LEN, CROSS_RATE, INITIAL_POPULATION, LINEAR_LAYER, LINEAR_LAYER_LEN, MAX_KERNAL, MIN_KERNAL, MUTATE_RATE, POOLING_LAYER, POOLING_LAYER_LEN

def init():
    population = []

    for i in range(INITIAL_POPULATION):
        ind = Individual(generate_individual())
        population.append(ind)
    
    return population

def get_layers(code, layer_type):
    list = []

    for i, v in enumerate(code):
        if v == layer_type:
            list.append(i)

    return list

def swap(code1, iv1, code2, iv2, layer_len):

    str1 = code1[iv1:iv1+layer_len]
    str2 = code2[iv2:iv2+layer_len]

    code1[iv1:iv1+layer_len] = str2
    code2[iv2:iv2+layer_len] = str1

    return code1, code2

def swap_layers(code1, code2, layer_type, layer_len):
    c1, c2 = get_layers(code1, layer_type), get_layers(code2, layer_type)
    min_c = min(len(c1), len(c2)) 

    for i in range(min_c):
        if random.random() < CROSS_RATE:
            index1 = random.randint(0, len(c1)-1)
            index2 = random.randint(0, len(c2)-1)

            iv1 = c1.pop(index1)
            iv2 = c2.pop(index2)
            
            code1, code2 = swap(code1, iv1, code2, iv2, layer_len)
    
    return code1, code2

def cross_code(code1, code2):
    code1, code2 = swap_layers(code1, code2, CONV_LAYER, CONV_LAYER_LEN)
    code1, code2 = swap_layers(code1, code2, POOLING_LAYER, POOLING_LAYER_LEN)
    code1, code2 = swap_layers(code1, code2, LINEAR_LAYER, LINEAR_LAYER_LEN)

    return code1, code2

def mutate(part, layer_type):

    if layer_type == CONV_LAYER and len(part) == CONV_LAYER_LEN:
        part[1] = int(part[1] * random.uniform(.9, 1.1))
        part[2] = random.randint(MIN_KERNAL, MAX_KERNAL)

    elif layer_type == POOLING_LAYER and len(part) == POOLING_LAYER_LEN:
        part[1] = random.randint(MIN_KERNAL, MAX_KERNAL)
    
    elif layer_type == LINEAR_LAYER and len(part) == LINEAR_LAYER_LEN:
        part[1] = int(part[1] * random.uniform(.9, 1.1)) 
    
    return part

def mutate_layer(code, layer_type, layer_len):

    layers = get_layers(code, layer_type)

    for layer in layers:
        if random.random() < MUTATE_RATE:
            code[layer:layer+layer_len] = mutate(code[layer:layer+layer_len], layer_type)

    return code
    

def mutate_code(code):
    if len(code) > CONV_LAYER_LEN:
        code = mutate_layer(code, CONV_LAYER, CONV_LAYER_LEN)
        code = mutate_layer(code, POOLING_LAYER, POOLING_LAYER_LEN)
        code = mutate_layer(code, LINEAR_LAYER, LINEAR_LAYER_LEN)

    return code