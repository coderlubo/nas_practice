import torch
from torch import nn
from utils.settings import DEVICE

loss_fn = nn.CrossEntropyLoss()
loss_fn = loss_fn.to(DEVICE)


def test_model(model, test_load):

    correct = 0.0
    test_loss = 0.0

    model.eval()
    with torch.no_grad():

        for data, target in test_load:
            data, target = data.to(DEVICE), target.to(DEVICE)

            output = model(data)

            test_loss += loss_fn(output, target).item()

            max_index = output.argmax(dim=1)
            correct += max_index.eq(target.view_as(max_index)).sum().item()

        test_loss /= len(test_load.dataset)
        accuracy = correct / len(test_load.dataset)

        # print("Test -- Average loss: {:.4f}, Accuracy : {:.3f}\n".format(test_loss, accuracy))

    return accuracy