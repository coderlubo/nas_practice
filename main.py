from utils.buildModel import build_model
from utils.dealCode import cross_code, mutate_code
from utils.evaluateModel import evaluate_model
from utils.generateOffspring import generate_offspring
from utils.getData import get_data
from utils.settings import INITIAL_POPULATION


train_load, eval_load, test_load = get_data()

population = []

for i in range(INITIAL_POPULATION):
    population.append(generate_offspring())


for code in population:

    model = build_model(code)
    # print(model)
    correct = evaluate_model(model, train_load, eval_load)


