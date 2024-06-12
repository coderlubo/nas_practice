def find_best(offspring):
    
    for i in range(len(offspring)):
        if hasattr(offspring[i], "fitness") == False:
            offspring[i].set_fitness()

    best_obj = max(offspring, key=lambda obj: obj.fitness)

    return best_obj