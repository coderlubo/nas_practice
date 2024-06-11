from torch import nn

from utils.settings import DEVICE

loss_fn = nn.CrossEntropyLoss()
loss_fn.to(DEVICE)

def train_model(model, train_load, optim):
    model.train()

    for batch_index, (data, target) in enumerate(train_load):
        data, target = data.to(DEVICE), target.to(DEVICE)

        optim.zero_grad()
        output = model(data)

        result_loss = loss_fn(output, target)
        result_loss.backward()

        optim.step()

        if batch_index % 300 == 0:
            
            print("batch index: {} \t  Loss:{:.6f}".format(batch_index, result_loss.item()))