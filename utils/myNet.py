from turtle import forward
from torch import nn

class Net(nn.Module):

    def __init__(self, model) -> None:
        super().__init__()
        self.model = model

    def forward(self, input):
        output = self.model(input)

        return output
