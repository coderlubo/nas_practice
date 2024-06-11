import torch
from utils.getData import get_data
from utils.myNet import Net
from utils.settings import DEVICE, EPOCHS
from utils.testModel import test_model
from utils.trainModel import train_model


def evaluate_model(model, train_load, eval_load):

    optim = torch.optim.Adam(model.parameters())

    for i in range(EPOCHS):
        train_model(model, train_load, optim)

        correct = test_model(model, eval_load)

    return correct


