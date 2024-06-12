def find_best(offspring, train_load, eval_load):
    
    for i in range(len(offspring)):
        if hasattr(offspring[i], "fitness") == False:
            offspring[i].set_fitness(train_load, eval_load)

    best_obj = max(offspring, lambda obj: obj.fitness)

    return best_obj