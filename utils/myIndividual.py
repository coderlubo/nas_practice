from venv import logger
import torch
from utils.buildModel import build_model
from utils.globalsVar import get_eval_data, get_global_logger, get_train_data
from utils.settings import EPOCHS
from utils.testModel import test_model
from utils.trainModel import train_model

class Individual:
    def __init__(self, code) -> None:
        self.code = code    

    def get_model(self):
        return self.model

    def set_fitness(self):
        logger = get_global_logger()
        train_load = get_train_data()
        eval_load = get_eval_data()

        self.model = build_model(self.code)

        optim = torch.optim.Adam(self.model.parameters())

        for i in range(EPOCHS):
            train_model(self.model, train_load, optim)

        fitness = test_model(self.model, eval_load)

        self.fitness = fitness

        logger.info("code: {}".format(self.code))
        logger.info("fitness: {}".format(self.fitness))