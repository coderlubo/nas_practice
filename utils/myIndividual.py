import torch
from utils.buildModel import build_model
from utils.settings import EPOCHS
from utils.testModel import test_model
from utils.trainModel import train_model


class Individual:
    def __init__(self, code) -> None:
        self.code = code    

    def get_model(self):
        return self.model

    def set_fitness(self, train_load, eval_load):

        self.model = build_model(self.code)

        optim = torch.optim.Adam(self.model.parameters())

        for i in range(EPOCHS):
            train_model(self.model, train_load, optim)

        fitness = test_model(self.model, eval_load)

        self.fitness = fitness